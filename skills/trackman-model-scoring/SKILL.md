---
name: trackman-model-scoring
description: Run or maintain the TrackMan model-scoring subsystem in baseball/ that turns pitch-by-pitch data into Stuff+, xWhiff, xSLG, and swing-decision value using the hitter-app/ and pitcher-app/ models. Use this whenever the user wants to score a TrackMan export, re-run enrich-trackman, add/swap/retrain a model, debug why Stuff+/xSLG look wrong, change the feature engineering or modelâ†’schema mapping, or understand how src/portal/trackman.py reproduces the Streamlit apps headless. Triggers on "Stuff+", "xSLG", "xWhiff", "decision value", "score the TrackMan file", "the pitcher/hitter models", "rapsodo/trackman csv", or any edit to trackman.py or the app model files. Reach for this before editing the scoring math â€” the feature engineering must match the apps exactly or the numbers drift.
---

# TrackMan model scoring

`src/portal/trackman.py` runs, headless, the exact math the two Streamlit apps run in their
UI, then aggregates to one season line per player and upserts into `stats_hitting` /
`stats_pitching` (source `"trackman"`). It is a normal enrichment adapter (see the
**portal-enrichment-adapter** skill for the resolve/upsert contract) â€” this skill covers the
model-specific parts that must stay faithful to the apps, or the metrics drift silently.

Entry point: `enrich_from_trackman(con, config)` â† CLI `python run.py enrich-trackman [--csv â€¦]`.
Default input is `pitcher-app/data/raw/usd_baseball_TM_master_file.csv` (standard TrackMan v3
columns); `load_trackman` lowercases headers to a canonical set.

**The apps (`hitter-app/`, `pitcher-app/`) are cloned repos with their own `.git`.** Reuse
their math; don't edit their model code as part of pipeline work. Model design is credited in
those repos to Thomas Nestico, Kyle Bland, Max Bay.

## Models

| Output | File (default dir) | Type | Features |
|---|---|---|---|
| TJ Stuff+ | `pitcher-app/models/NCAA_STUFF_PLUS_ALL.joblib` | sklearn Pipeline â†’ **LightGBM** | release/movement (below) |
| xWhiff | `pitcher-app/models/whiff_model_grouped_training.joblib` | sklearn Pipeline â†’ **RandomForest** | same feature list as Stuff+ |
| xSLG | `hitter-app/models/xSLG_model.json` | **XGBoost** booster | launch_speed, launch_angle, interaction |
| decision value | `hitter-app/models/model_{swing,no_swing}.json` | **XGBoost** boosters | Platelocside, Platelocheight, strikes, balls |

Deps are **lazy-imported** via `trackman._need(...)`: `xgboost`, `scikit-learn`, `lightgbm`,
`joblib` (in `requirements.txt` as optional). Without them, scoring returns a `skipped: â€¦`
message and the rest of the pipeline runs. Install: `pip install xgboost scikit-learn lightgbm joblib`.

## Pitcher path (Stuff+ / xWhiff)

`score_pitching(df, models_dir)`:
1. `_process_relheight`-equivalent smoothing is folded in via the apps; we then engineer
   features in `_pitcher_features`:
   - Derive `pitcher_hand` from the **sign of mean RelSide** (not PitcherThrows) â€” the model
     expects all arms normalized to one frame, so for LHP we **negate `ax` (HorzBreak) and
     `x0` (RelSide)**. Get this wrong and lefties score garbage.
   - Rename to model space: `start_speed`=RelSpeed, `spin_rate`=SpinRate, `z0`=RelHeightÂ·12,
     `x0`=RelSideÂ·12, `ax`=HorzBreak, `az`=InducedVertBreak.
   - `speed_diff/az_diff/ax_diff` are **relative to the pitcher's own primary fastball**
     (dominant of Four-Seam/Sinker by count); `is_fastball` flags those two AutoPitchTypes.
2. Predict with the LightGBM pipeline â†’ `target`, then scale to Stuff+ with the **frozen 2023
   calibration**: `tj_stuff_plus = 100 âˆ’ 10Â·(target âˆ’ 0.011532333993710725)/0.009399038486978739`.
   Mean â‰ˆ 100, Ïƒ â‰ˆ 10. Don't change these constants without re-deriving from the same training set.
3. xWhiff uses the **same feature frame**; it's optional sugar â€” wrapped in try/except so a
   whiff-model failure never blocks Stuff+.

`aggregate_pitching` â†’ per pitcher: `t2_stuff` (mean Stuff+), per-pitch `*_stuff` and
`*_strike_pct` (AutoPitchType â†’ cb/ch/ct/fb/si/sl via `_PITCH_CODE`), plus observed
`inzone_whiff_pct`, `chase_pct`, `strike_pct`, `miss_pct`, `ground_pct`, `hardhit_pct`,
modeled `xwhiff_pct`, and `pitches`.

## Hitter path (xSLG / decision value)

`score_hitting(df, models_dir)`:
- **xSLG** on batted balls only (`ExitSpeed > 0`): features `launch_speed`=ExitSpeed,
  `launch_angle`=Angle, `interaction`=ExitSpeedÂ·Angle; predict via `xgb.DMatrix` with those
  exact feature names.
- **decision value**: the hitter app **negates PlateLocSide** before splitting takes/swings â€”
  replicate it. Takes â†’ `model_no_swing`, swings â†’ `model_swing`, on
  `[Platelocside(negated), Platelocheight, strikes, balls]`.

`aggregate_hitting` â†’ per batter: `xslg` (mean over swings), `decision_value`
(`_scale_20_80` of mean decision_rv with the app's overall Î¼=âˆ’0.0032, Ïƒ=0.0130), `avg_ev`,
`ev90`, `hardhit_pct` (>90), `barrel_pct` (EVâ‰¥99 & LA 25â€“31), `gb_pct`, `pull_pct`, `k_pct`
(from KorBB over PA), `chase_pct`, `zcon_pct`, `swstr_pct`, `pa`, `pitches`.

## Event flags (TrackMan-standard, shared)

`_pitch_flags` defines: `whiff` = PitchCall `StrikeSwinging`; `swing` = whiff | foul | inplay
(or ExitSpeed>0); `strike` adds called strikes; `inzone` = PlateLocSideâˆˆ[âˆ’0.83,0.83] &
PlateLocHeightâˆˆ[1.5,3.5]. These feed chase/zone/whiff rates; keep them consistent across both
paths.

## Common tasks

- **Score a different export:** `python run.py enrich-trackman --csv path-or-url`. Any TrackMan
  v3 CSV works (Rapsodo/Trackman). Use this for a transfer target's own data, not just USD's.
- **Swap/retrain a model:** drop the new file in the app's `models/` dir (or point
  `enrichment.trackman.{hitter,pitcher}_models` at another dir). Keep the feature list and,
  for Stuff+, the calibration constants in sync â€” if the new model changes the target
  distribution, re-derive the mean/Ïƒ.
- **Add a new modeled metric:** compute it per pitch in `score_*`, aggregate it in
  `aggregate_*`, map it to a schema column (add the column + migrate if new â€” see the
  enrichment-adapter skill), and add it to the `evaluate.py` metric list so it moves fit.

## Gotchas

- **sklearn version skew:** the `.joblib` pipelines were pickled on sklearn 1.3; current envs
  load them with a newer sklearn (verified working on 1.8 with only a warning). If loading
  fails after a sklearn upgrade, pin closer to 1.3 rather than rewriting the model.
- **Feature fidelity:** the LHP sign flips, fastball-relative diffs, the Â·12 inch conversion,
  and the plate-side negation for decisions are the easy things to break. Changing any of them
  silently shifts every number. Re-run the smoke check after edits.
- **Smoke check after edits:** load the master CSV, `score_pitching` + `score_hitting`, and
  confirm Stuff+ centers ~97â€“100 (Ïƒâ‰ˆ10) and per-batter xSLG lands ~0.2â€“0.7. Wildly off â†’
  feature engineering broke.
- **Names are "Last, First"** in TrackMan; the `Resolver` handles ordering, but verify
  `matched`/`created` counts look sane against the DB after a run.
