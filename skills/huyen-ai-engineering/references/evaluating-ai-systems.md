# Evaluating AI Systems: criteria, model selection, and the eval pipeline (Huyen Ch. 4)

## Produce
Three linked artifacts: (1) an **evaluation criteria set** for the application (domain capability, generation capability, instruction-following, cost/latency) with the method that measures each; (2) a **model-selection decision** â€” build-vs-buy (API vs. self-host) plus the 4-step filterâ†’benchmarkâ†’experimentâ†’monitor workflow with a hard-vs-soft attribute split; and (3) a **custom evaluation pipeline** (per-component + per-turn + per-task, scoring rubric, metricsâ†’business-metrics map, annotated slices, sample-size/reliability checks).

This is the second crown-jewel doc â€” it *operationalizes* the methods in `evaluation-methodology.md`. Fire it when someone is building the eval harness, picking a model, or asking "is my eval reliable / how many samples do I need?"

## Trigger checks
- "How do I pick the right model for my app?" / "Should we use an API or self-host?"
- "What criteria/metrics should I evaluate?" (factual consistency, safety, instruction-following, latency)
- Building an eval pipeline / harness; "my eval isn't reliable / reproducible"
- Trusting (or not) public benchmarks and leaderboards; data contamination worries
- "How big should my eval set be?" / mapping eval metrics to business impact
- Interview: "Walk me through building an evaluation pipeline" / "How would you do model selection?"

## Evaluation-driven development (the framing)
Define evaluation criteria *before* building (test-driven development's cousin). The worst outcome isn't a non-deployed app â€” it's a *deployed app nobody can tell is working* (costs to run, costs more to remove). Eval is "the biggest bottleneck to AI adoption." But beware the lamppost trap: don't restrict to only easily-measurable use cases â€” that's where the key isn't.

## How to apply

### Part 1 â€” Define evaluation criteria (given a criterion, which method?)
Four buckets, illustrated by "summarize a legal contract": **domain-specific capability** (understands legal text), **generation capability** (coherent/faithful summary), **instruction-following** (right format/length), **cost & latency** (price + wait).
- **Domain-specific** â†’ exact eval where possible. Coding â†’ functional correctness, but also care about *efficiency* (runtime/memory; BIRD-SQL grades query runtime) and *readability* (subjective â†’ AI judge). Non-coding â†’ close-ended MCQ (75% of lm-eval-harness tasks): easy to verify, has a random baseline (4-option â†’ 25%), good for *knowledge/reasoning*. Caveat: MCQ tests *discrimination*, not *generation*; sensitive to tiny prompt changes (extra space, "Choices:").
- **Generation** â†’ older NLG metrics (fluency, coherence) now matter less (outputs are human-like) except for weak models/creative/low-resource. New issues need new metrics: **factual consistency** and **safety**.
  - **Factual consistency**: split **local** (against given context â€” summarization, support, analysis; far easier) vs. **global** (against open knowledge â€” hardest part is *deciding what the facts are*). Methods: AI-as-judge (GPT-3.5/4 beat prior methods; GPT-judge 90â€“96%), **self-verification** (SelfCheckGPT â€” sample N, measure agreement; expensive), **knowledge-augmented** (SAFE â€” decompose â†’ self-contain â†’ search â†’ verify), or frame as **textual entailment** (entailment/contradiction/neutral) with a small specialized classifier (DeBERTa-NLI). Benchmark: TruthfulQA (817 Qs; human 94%). Critical for RAG. Tip: profile *what kinds* of queries hallucinate (niche knowledge, things that don't exist) and weight the benchmark there.
  - **Safety**: categories â€” inappropriate language, harmful tutorials, hate speech, violence, stereotypes, ideological bias. Use small specialized toxicity classifiers (Perspective API) or general judges + moderation endpoints. Benchmarks: RealToxicityPrompts, BOLD.
- **Instruction-following** â†’ IFEval (25 auto-verifiable instruction types: keywords, length, format, JSON) and INFOBench (broader â€” content/linguistic/style constraints verified via per-instruction yes/no criteria; GPT-4 a reliable evaluator). **Roleplaying** is a top real-world instruction type â€” evaluate both *style* and *knowledge* (incl. negative knowledge: an NPC shouldn't reveal what the character wouldn't know). **Curate your own instruction benchmark** â€” public ones miss your instructions. Trap: poor output may be a *bad instruction*, not a bad model.
- **Cost & latency** â†’ Pareto optimization: declare what you *can't* compromise (e.g., latency), filter on it, then pick the best of the rest. Latency metrics: TTFT, TPOT, time-between-tokens, per-query â€” know which matters. Latency is usually an annoyance (nice-to-have), not a deal-breaker (must-have). Cost: APIs charge per token (flat per-token at scale); self-hosting = compute (per-token drops with scale â†’ re-evaluate API-vs-host at each scale). Build a criteria table with metric + benchmark + hard requirement + ideal.

### Part 2 â€” Model selection
- **Hard vs. soft attributes**: hard = can't/won't change (license, training data, size, privacy policy, latency if not self-hosted) â†’ filter first. Soft = improvable (accuracy, toxicity, latency if self-hosted) â†’ estimate realistic lift (one task jumped 20%â†’70% after decomposition; another stayed unusable after weeks).
- **4-step workflow**: (1) filter on hard attributes â†’ (2) narrow with public benchmarks/leaderboards balancing quality/latency/cost â†’ (3) run *your own* eval pipeline on the shortlist â†’ (4) monitor in production. Iterative â€” later steps can revise earlier decisions.
- **Build vs. buy (API vs. self-host)** across **seven axes**: **data privacy** (Samsung leak; API may train on your data), **data lineage/copyright** (opaque training data; commercial contracts can indemnify; open-data lets you audit), **performance** (best models stay closed; gap closing but incentives keep the strongest proprietary ahead), **functionality** (APIs more likely to offer scaling/function-calling/structured-output/guardrails but often hide logprobs; self-host exposes logprobs + intermediate states, key for classification/eval/interpretability), **cost** (API per-usage vs. engineering cost to host â€” "APIs are expensive, but engineering can be even more so"), **control/access/transparency** (rate limits, silent model updates breaking prompts, risk of losing access; self-host lets you *freeze* a model), **on-device** (APIs out). Terminology: open weight (no data) vs. open model (with data); check license for commercial use, MAU limits (Llama: 700M), and whether outputs can train other models (distillation).

### Part 3 â€” Navigate public benchmarks (filter, don't select)
Thousands exist (BIG-bench: 214); use an **evaluation harness** (lm-evaluation-harness 400+, OpenAI evals ~500). Leaderboards aggregate a *small* subset (HF: 4â†’6 benchmarks; HELM: 10) with opaque selection and different choices â†’ hard to compare. Watch **benchmark correlation** (drop redundant strongly-correlated ones â€” WinoGrande/MMLU/ARC-C all reasoning; correlated benchmarks exaggerate bias). Aggregation differs: HF averages (treats all equal); HELM uses mean win rate. **Data contamination** is rampant ("training on the test set"; "Pretraining on the Test Set Is All You Need" got near-perfect scores from a 1M-param model) â€” often unintentional (scraped benchmarks) or even intentionally-good (training on benchmark data improves the released model). Detect via **n-gram overlap** (accurate, needs training data) or **perplexity** (unusually low on eval data â†’ likely seen). **Public benchmarks filter out bad models; they don't find your best model.** Running them is costly (HELM: ~$80â€“100k for 30 models).

### Part 4 â€” Design your evaluation pipeline (the deliverable)
1. **Evaluate all components + levels.** Per-component (PDFâ†’text, then textâ†’employer â€” isolate where it fails), per-turn (output quality), per-task (did it complete? how many turns? â€” most important to users, but task boundaries are fuzzy).
2. **Create an evaluation guideline** (most important step). Define what the app should AND shouldn't do (out-of-scope handling). Define criteria (LinkedIn: "you're a terrible fit" is *correct but not good*; avg 2.3 criteria/app). Build a **scoring rubric with examples** (binary / 1â€“5 / entailment-style) and validate it with humans â€” if humans can't follow it, refine. **Tie metrics to business metrics** (factual consistency 80%â†’automate 30%; 90%â†’50%; 98%â†’90%) and set the **usefulness threshold**. Understand the upstream business metric (DAU/WAU/MAU, engagement) and its ethics tradeoffs.
3. **Define methods + data.** Mix methods per criterion (cheap classifier on 100% + expensive AI judge on 1%). Use **logprobs** when available (confidence, perplexity). Keep **human evaluation** as a North Star (LinkedIn: 500 daily convos). Plan for *production* eval (no reference data, but real users + feedback). **Annotate** data (reuse the guideline for finetuning later). **Slice** the data â€” per-component, per-criterion, by tier/traffic/usage, a known-failure set, an out-of-scope set â€” to avoid bias and **Simpson's paradox** (A beats B on every subgroup yet loses overall). Reuse the rubric for annotation.
4. **Size the eval set + check reliability.** Big enough to trust, small enough to afford. **Bootstrap** (resample with replacement) to test stability â€” wildly varying results â†’ need more data. To detect a *difference* between systems at 95% confidence (OpenAI rule): 30%â†’~10, 10%â†’~100, 3%â†’~1,000, 1%â†’~10,000 (every 3Ã— smaller difference â†’ 10Ã— more samples). lm-eval-harness median ~1,000; Inverse-Scaling minimum ~300.
5. **Evaluate the evaluation pipeline.** Right signals (better responses score higher; better metrics â†’ better business)? Reliable (rerun variance; set AI-judge temperature to 0)? Metric correlation? Cost/latency it adds (don't skip eval to cut latency â€” risky bet)?
6. **Iterate with experiment tracking** â€” log eval data, rubric, judge prompt + sampling config. Iterate, but keep enough consistency to track the app over time.

## Common failure modes
- **Public-leaderboard worship.** Picking the top-ranked model when its leaderboard has no benchmark for your use case (code, summarization, tool use).
- **No per-component eval.** Only scoring end-to-end, so you can't localize the failing step.
- **Vague guideline.** Ambiguous "good" â†’ ambiguous scores; correct-but-unhelpful responses pass.
- **Metrics untethered from business.** Reporting "82% coherence" with no link to tickets automated / revenue.
- **Eval-set too small / unbootstrapped.** Declaring a new prompt "better" on a swing that's within noise.
- **Drifting judge / unlogged config.** AI-judge temperature â‰  0, prompt changes untracked â†’ unreproducible.
- **Ignoring contamination.** Trusting bar-exam scores as legal-advice ability when the benchmark was in training data.
- **Build-vs-buy by vibe.** Choosing self-host/API without scoring the seven axes against *this* use case and scale.

## Interview signal
**AI-Engineer / FDE framing:** This is the deepest applied-AI competency. Senior signal = evaluation-driven development (criteria before code), per-component + per-task decomposition, a rubric tied to a business metric with a usefulness threshold, the bootstrap/sample-size discipline, and treating public benchmarks as a *filter* not a selector (contamination-aware). For FDE specifically, the build-vs-buy reasoning across the seven axes (privacy, lineage, control, cost-vs-engineering) is exactly the customer conversation.
**One crisp talking point:** *"I do evaluation-driven development: before building I write the criteria and a scoring rubric with examples, then tie each metric to a business metric and a usefulness threshold â€” 'factual consistency of 90% lets us automate 50% of tickets.' I evaluate every component and the whole task, slice the data to dodge Simpson's paradox, and bootstrap to know my eval set is big enough â€” every 3Ã— smaller difference I want to detect needs 10Ã— the samples. Public benchmarks only filter out bad models; they're contaminated and don't match my distribution, so the real selection happens on my own pipeline."*

## Practitioner checklist
- [ ] Criteria defined across all four buckets (domain, generation, instruction-following, cost/latency) with a measurement method per criterion
- [ ] Factual consistency scoped local vs. global; safety categories chosen; own instruction benchmark curated
- [ ] Build-vs-buy decided against the seven axes for this use case + scale; license checked
- [ ] Hard attributes filtered first; soft-attribute lift estimated realistically; 4-step workflow run
- [ ] Public benchmarks used only to shortlist; correlation + contamination considered
- [ ] Pipeline evaluates per-component, per-turn, per-task
- [ ] Scoring rubric with examples, human-validated; metrics mapped to business metrics + usefulness threshold
- [ ] Data sliced (incl. known-failure + out-of-scope sets); eval-set size justified via bootstrap / the OpenAI sample-size rule
- [ ] Eval pipeline itself evaluated (signal, reliability w/ judge temp=0, correlation, added cost/latency); configs logged

## References
- *AI Engineering* (Huyen, O'Reilly 2024), Ch. 4 (pp. 315â€“415): Evaluation Criteria, Model Selection (build-vs-buy, public benchmarks, contamination), Design Your Evaluation Pipeline.
- Sibling docs: **`evaluation-methodology.md`** (the methods this chapter deploys â€” read first), `planning-ai-applications.md` (usefulness threshold origin), `prompt-engineering.md` (instruction-following + judge prompting), `rag-and-agents.md` (evaluating retrieval/agents), `inference-optimization.md` (cost/latency mechanics), `architecture-and-user-feedback.md` (production monitoring + feedback as eval).
- Related skills: `kohavi-controlled-experiments` (A/B testing the business-metric lift online), `mlsd-coach` (eval section of an ML system-design interview), `claude-api` (logprobs availability, model-version transparency).
