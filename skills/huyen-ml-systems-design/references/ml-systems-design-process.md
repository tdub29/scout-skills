# Huyen â€” ML Systems Design Process (framing, objectives, requirements, iteration)

**Produce this:** a one-page **ML problem frame + design contract** â€” business objective â†’ ML objective(s) (decoupled), the task type and I/O, the four requirements (reliability / scalability / maintainability / adaptability) with concrete targets, and the iterative loop you'll run. This is the artifact you open *every* ML system design interview with, before you touch a model.

## When to pull this

- "Design an ML system for X" â€” the opening 5 minutes, before architecture.
- Someone hands you a business problem ("speed up customer support", "increase engagement") and you must turn it into an ML task.
- You have multiple objectives in tension (engagement vs. quality, precision vs. recall, revenue vs. trust).
- You're being asked for non-functional requirements / "how do you know it's a *good* system".
- Scoping a real project and need to tie ML metrics to a business metric so it doesn't get killed.

Don't pull this for the *details* of any single stage â€” route to `training-data`, `feature-engineering`, `offline-evaluation`, `model-deployment`, `data-distribution-shifts-and-monitoring`, or `continual-learning-and-test-in-production`. This doc is the spine that sequences them.

## The framework

### 1. Business objective â†’ ML objective (the translation that keeps projects alive)
Companies do not care about accuracy 94% â†’ 94.2%. They care about a **business metric**: revenue (conversion, ads, cost cut) directly, or satisfaction / time-on-site / retention indirectly. The #1 way ML projects die: the DS hacks ML metrics nobody can map to business value, the manager sees no business movement, and kills it.

Your job: name the business metric, then construct the ML metric that *moves it*, and state the causal chain explicitly. Netflix's **take-rate** (quality plays Ã· recommendations shown) is the model: an ML-measurable proxy they validated against streaming hours and cancellation rate. When the mapping is direct (CTR â†’ ad revenue; fraud caught â†’ money saved) the project is easy to justify â€” that's *why* ad CTR and fraud are the canonical ML use cases. When ML is one component in a long pipeline (anomaly â†’ rules â†’ human review â†’ mitigation), the contribution may be **un-attributable** â€” flag that.

Two honest caveats to state out loud: returns on ML scale with **adoption maturity** (years in production â†’ faster deploys, lower cost), and the effect on business metrics usually requires an **experiment (A/B)** to pin down â€” pick the model that moves the *business* metric even if its ML metric is worse.

### 2. Frame the ML problem: inputs, outputs, objective function
"Slow support" is a problem, not an ML problem. An ML problem = **(inputs, outputs, objective function)**. The framing you choose changes the difficulty dramatically.

- **Task type follows the output.** Classification vs. regression are interconvertible (bucket a price â†’ classification; threshold a probability â†’ regression). Within classification: **binary** (easiest â€” F1 and confusion matrices are intuitive) â†’ **multiclass** â†’ **high-cardinality** (1000s of classes: needs ~100+ examples/class, so 100k+ examples; rare classes starve) â†’ consider **hierarchical** (coarse classifier then fine classifier). **Multilabel** (example âˆˆ multiple classes) is the one teams get wrong most: it breaks annotation (label multiplicity / annotator disagreement) and makes extracting predictions from raw probabilities ambiguous (how many of [0.45,0.2,0.02,0.33] do you keep?).
- **Reframing changes the cost of change.** "Predict next app" as multiclass over N apps (output = vector of size N) forces a **full retrain whenever an app is added**. Reframe as regression â€” input = (user, environment, *app*) features, output = one score per (user, app) â€” and a new app is just new input, no retrain. **Prefer framings where new entities don't force retraining.**

### 3. Objective functions, and *decoupling* multiple objectives
The objective (loss) function guides learning â€” usually a standard one: RMSE/MAE (regression), log loss (binary), cross-entropy (multiclass). The senior move is handling **multiple, conflicting objectives**.

Newsfeed example: rank by `engagement` vs. rank by `quality` conflict (extreme content is engaging but low quality). Two ways to combine:
- **Single model, combined loss:** `loss = Î±Â·quality_loss + Î²Â·engagement_loss`. Problem: every retune of Î±/Î² requires a **full retrain**. (Use Pareto optimization to tune systematically.)
- **Decoupled models:** train `quality_model` and `engagement_model` separately, then rank by `Î±Â·quality_score + Î²Â·engagement_score`. Now you tune Î±/Î² **without retraining**.

**Default to decoupling.** Two wins: (1) tweak the tradeoff without retraining; (2) independent maintenance schedules â€” spam evolves faster than perceived post-quality, so the spam model retrains far more often.

### 4. The four requirements (state targets, not adjectives)
- **Reliability** â€” correct function at desired performance under faults/human error. The ML twist: **silent failures**. `model.predict()` returns no error but the prediction is wrong, and with no ground truth at serving time users keep using a broken system (bad translation looks fine to someone who doesn't speak the language). â†’ forces the monitoring story (Ch8).
- **Scalability** â€” three axes: **complexity** (1GB logistic regression â†’ 16GB neural net), **traffic** (10k â†’ 10M req/day), and **model count** (1 model â†’ 8000 models, one per enterprise customer). Resource scaling (autoscaling up/down â€” note Amazon's Prime Day autoscale failure cost ~$72â€“99M) is only half; the other half is **artifact management** â€” monitoring/retraining/reproducing 100 models is categorically different from 1.
- **Maintainability** â€” many owners (ML eng, DevOps, SMEs, different tools/languages). Version code+data+artifacts, document, make models reproducible so work survives the original author leaving, enable blameless cross-team debugging.
- **Adaptability** â€” capacity to discover improvements *and* push updates without service interruption, because data shifts fast (links to drift Ch8 + continual learning Ch9).

### 5. The iterative process (it's a cycle, not a line)
1. **Project scoping** â€” goals, objectives, constraints, stakeholders, resource estimate.
2. **Data engineering** â€” sources/formats (Ch3) â†’ curate training data: sample + label (Ch4).
3. **ML model development** â€” feature engineering (Ch5), model selection/training/eval (Ch6).
4. **Deployment** â€” make it accessible (Ch7); "you never finish, you ship."
5. **Monitoring + continual learning** â€” watch for decay, adapt (Ch8, Ch9).
6. **Business analysis** â€” evaluate against business goals, generate insight, loops back to step 1.

The real workflow back-tracks constantly: relabel after error analysis â†’ retrain â†’ discover 99.99% negative class â†’ collect more positives â†’ retrain â†’ model is stale on yesterday's data â†’ retrain â†’ ship â†’ revenue drops because nobody clicks â†’ **change the objective from impressions to CTR â†’ go to step 1.** Narrate this loop in an interview; linear "collectâ†’trainâ†’deployâ†’done" reads junior.

### Mind vs. data (one-liner, don't dwell)
Modern ML success tracks **data quantity *and* quality** far more than algorithmic cleverness (Norvig: "we don't have better algorithms, we just have more data"; Sutton's Bitter Lesson). But more data at *lower* quality (stale, mislabeled) can hurt. Use this only if asked "what matters more, model or data" â€” answer: data, conditioned on quality; finite data is necessary, the open question is whether it's *sufficient*.

## How to apply (interview opening sequence)
1. **Restate the business objective and the metric it moves.** "We want to increase purchase-through rate / cut fraud loss / raise take-rate." If you can't name it, ask.
2. **Build the ML-to-business causal chain.** State the proxy ML metric and how a unit of it maps to the business metric; flag if attribution requires an A/B test or if ML is un-attributable inside a longer pipeline.
3. **Frame the ML problem as (inputs, outputs, objective function).** Name the task type from the output. Choose the framing that avoids retrain-on-new-entity.
4. **List objectives; decouple if >1 and they conflict.** Propose separate models + a tunable `Î±Â·scoreâ‚ + Î²Â·scoreâ‚‚` combiner; justify with the no-retrain + independent-maintenance argument.
5. **State the four requirements with concrete targets** â€” reliability (incl. silent-failure detection), scalability (which axis: complexity/traffic/model-count + autoscaling + artifact mgmt), maintainability (versioning/reproducibility), adaptability (drift + continual learning).
6. **Sketch the iterative loop and where you'll back-track** â€” name the most likely loop (relabel? collect positives? change the objective?).
7. **Sanity-check:** could a skeptical EM kill this for "no business impact"? If yes, your step-1/step-2 mapping is too weak â€” redo it.

## Interview signal
This *is* the MLSD interview's opening and its connective tissue. Interviewers score whether you **clarify and frame before designing** (mlsd-coach Phase 1) and whether you tie ML to business value. Two crisp talking points:
- *"Before I pick a model I'd nail the framing: inputs, outputs, objective function â€” and I'd choose the framing that doesn't force a retrain when a new app/item/customer appears, e.g. score-per-(user,item) regression over an N-way classifier."*
- *"With conflicting objectives like engagement vs. quality I'd decouple into separate models and combine scores as Î±Â·quality + Î²Â·engagement, so we can retune the tradeoff in production without retraining and let each model follow its own retrain cadence â€” spam moves faster than perceived quality."*

## Practitioner checklist
- [ ] Business metric named, and the ML-metric â†’ business-metric chain is explicit (and falsifiable via A/B).
- [ ] Problem framed as (inputs, outputs, objective function); task type matches the output.
- [ ] Framing avoids full-retrain when a new class/entity is added (prefer per-entity scoring).
- [ ] Multilabel hazards checked (annotation multiplicity; prediction-extraction ambiguity).
- [ ] Multiple objectives decoupled into separate models + tunable combiner.
- [ ] Requirements quantified: reliability (silent-failure detection plan), scalability (axis + autoscale + artifact mgmt), maintainability (versioned code/data/artifacts, reproducible), adaptability (drift + continual-learning hook).
- [ ] Iterative loop drawn with the likely back-track points named.
- [ ] "Could an EM kill this for no business impact?" â€” answered no, with evidence.

## References
- Chip Huyen, *Designing Machine Learning Systems* (O'Reilly, 2022), Ch. 2 "Introduction to ML Systems Design" (pp. 50â€“78). Folds the Ch. 1 overview.
- Sibling references: `references/training-data.md`, `references/feature-engineering.md`, `references/offline-evaluation.md`, `references/model-deployment.md`, `references/data-distribution-shifts-and-monitoring.md`, `references/continual-learning-and-test-in-production.md`, `references/data-engineering-fundamentals.md`.
- Sibling skills: `mlsd-coach` (live drill), `kohavi-controlled-experiments` (the A/B test that resolves business-metric questions), `provost-data-science-for-business` (business-value framing), `kleppmann-data-intensive-systems` (the reliability/scalability/maintainability vocabulary at the systems layer).
