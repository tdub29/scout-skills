---
name: huyen-ml-systems-design
description: "ML system design interviews and production ML."
---

# huyen-ml-systems-design

Book provenance: **Chip Huyen â€” Designing Machine Learning Systems (O'Reilly, 2022)**. Carved for an Applied/Product DS + ML-system-design interview prep + practitioner lens. Load the matching `references/*.md` file when a specific stage of the ML lifecycle is in play.

## When to use

Use this hub when the user is **designing an ML system, prepping an MLSD/Applied-DS interview, or making a production-ML decision** that maps to a stage in the lifecycle. Route to **one** reference, read it fully, then produce that stage's artifact (decision tree, checklist, tradeoff table, diagnosis, or interview talking point) â€” not a book summary.

Don't improvise a hybrid across stages unless the user explicitly wants an end-to-end pass. For an end-to-end mock, walk the framework below and pull each reference in order.

## The end-to-end design framework at a glance

Huyen's lifecycle is an **iterative loop**, not a waterfall. Walk it in interviews:

1. **Frame** â€” business objective â†’ ML objective(s) â†’ inputs/outputs/loss â†’ reliability/scalability/maintainability/adaptability. *(`ml-systems-design-process`)*
2. **Data stack** â€” sources, storage, dataflow, batch vs stream. *(`data-engineering-fundamentals`)*
3. **Training data** â€” sampling, labeling, imbalance, augmentation. *(`training-data`)*
4. **Features** â€” operations, leakage audit, good-feature scorecard. *(`feature-engineering`)*
5. **Model + offline eval** â€” baselines, robustness/fairness/calibration/slice battery. *(`offline-evaluation`)*
6. **Deploy** â€” batch vs online, cloud vs edge, compression. *(`model-deployment`)*
7. **Monitor** â€” failure taxonomy, shift types, detection, feedback loops. *(`data-distribution-shifts-and-monitoring`)*
8. **Update + test in prod** â€” stateless vs stateful, cadence, shadow/A-B/canary/bandits. *(`continual-learning-and-test-in-production`)*
9. **Business analysis** â†’ back to step 1.

The senior framing: state the **business metric and the MLâ†’business map first**, present the lifecycle as a **loop**, and treat ML systems as **part code, part data** that **fail silently** and **decay over time**.

## Quick routing

| User cue (examples) | Reference |
|---|---|
| "Design an ML system for X", frame a vague ask, tie ML metric to business metric, decouple conflicting objectives, task framing, set RSMA requirements | `references/ml-systems-design-process.md` |
| Where data lives / moves, format (Parquet/CSV), relational vs document vs graph, OLTP vs OLAP, batch vs stream, static vs dynamic features | `references/data-engineering-fundamentals.md` |
| How to get/label data, sampling method + bias, natural vs hand labels, feedback-loop length, weak/semi/transfer/active learning, class imbalance | `references/training-data.md` |
| Feature operations, scaling, categorical/hashing trick, feature crossing, **data leakage**, feature importance vs generalization | `references/feature-engineering.md` |
| Model selection, baselines, "is it good?", perturbation/invariance/calibration/**slice-based** evaluation before deploy | `references/offline-evaluation.md` |
| Batch vs online prediction, cloud vs edge, latency budget, quantization/distillation/pruning, train-serve skew from two pipelines | `references/model-deployment.md` |
| "Worked at launch, degraded now", covariate/label/concept shift, drift detection without labels, degenerate feedback loops, what to monitor | `references/data-distribution-shifts-and-monitoring.md` |
| "How often to retrain", stateless vs stateful, champion/challenger, shadow/A-B/canary/interleaving/bandits, test in production | `references/continual-learning-and-test-in-production.md` |

## How to apply

1. Match the request to a row in **Quick routing** (or the description triggers).
2. Read the corresponding file under `references/`.
3. Follow that reference's decision flow, produce its artifact, and end with its **Interview signal** + **practitioner checklist** where relevant.
4. For a full mock loop, walk the framework above and pull references 1â†’8 in order.

## Infrastructure & human factors (Ch10-11, folded)

These chapters don't carry their own reference doc â€” surface the interview-relevant nuggets inline when they come up:

- **Infra (Ch10):** four layers â€” storage/compute, resource management (Airflow/Kubeflow), ML platform (**model store**, **feature store**, monitoring), dev environment. A **feature store** is the canonical fix for batch/stream feature consistency (the train-serve skew of `model-deployment`). A **model store** + lineage is the prerequisite for stage-2/3 continual learning. Default to **build-vs-buy = buy/adapt** at "reasonable scale" (GB-TB/day, not petabytes); most companies aren't FAANG-scale.
- **Human side (Ch11):** ML is **probabilistic** â†’ manage the **consistency-accuracy trade-off** (Booking.com pinned filter recs with rules); **"mostly correct" predictions** need a **human-in-the-loop** UI (show k candidates the user can pick/edit); **smooth failing** via a fast backup heuristic; **team structure** â€” keep model dev and deployment close to avoid handoff bugs; **responsible AI** â€” fairness via the invariance tests in `offline-evaluation`, bias amplified by the feedback loops in `data-distribution-shifts-and-monitoring`.

## Common failure modes (hub-level)

- **Skipping the frame.** Jumping to "I'd train XGBoost" without the business metric, I/O, and requirements â€” the #1 junior tell. Always start at `ml-systems-design-process`.
- **Router-only answer.** Summarizing the hub without loading the reference's full framework + artifact.
- **Wrong reference.** Loading "offline eval" when the question is about online A/B testing (that's `continual-learning-and-test-in-production`), or "data engineering" depth that actually belongs in `kleppmann-data-intensive-systems`.
- **One-metric thinking.** Reporting a single F1 with no baseline or slice â€” route to `offline-evaluation`.
- **Treating deploy as the end.** Forgetting that models decay and need monitoring + continual learning.

## References

- [references/ml-systems-design-process.md](references/ml-systems-design-process.md) â€” frame the problem (Ch1-2)
- [references/data-engineering-fundamentals.md](references/data-engineering-fundamentals.md) â€” the data stack (Ch3, lighter; defers to Kleppmann)
- [references/training-data.md](references/training-data.md) â€” sampling, labeling, imbalance (Ch4)
- [references/feature-engineering.md](references/feature-engineering.md) â€” features + leakage (Ch5)
- [references/offline-evaluation.md](references/offline-evaluation.md) â€” baselines + eval battery (Ch6)
- [references/model-deployment.md](references/model-deployment.md) â€” batch/online, cloud/edge, compression (Ch7)
- [references/data-distribution-shifts-and-monitoring.md](references/data-distribution-shifts-and-monitoring.md) â€” shifts + monitoring (Ch8)
- [references/continual-learning-and-test-in-production.md](references/continual-learning-and-test-in-production.md) â€” retraining + online eval (Ch9)

- **Book:** Chip Huyen â€” *Designing Machine Learning Systems: An Iterative Process for Production-Ready Applications* (O'Reilly, 2022).
- **Sibling skills:**
  - `mlsd-coach` â€” drills these frameworks live as a mock ML-system-design interviewer (pair this hub as the reference, mlsd-coach as the rehearsal).
  - `kohavi-controlled-experiments` â€” the deep treatment of A/B testing (randomization, sample size, significance) that `offline-evaluation` and `continual-learning-and-test-in-production` point to.
  - `kleppmann-data-intensive-systems` â€” distributed-systems / storage-engine internals beneath the data layer (Huyen defers Ch3 depth here).
  - `provost-data-science-for-business` â€” business-value framing, baselines, profit/expected-value curves, leakage-as-overfitting.
  - `huyen-ai-engineering` â€” the companion volume for foundation-model / LLM application engineering (evaluation, prompting, RAG, finetuning, inference optimization). Route there for FM/LLM work; route here for classical/production ML systems.
