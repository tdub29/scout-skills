# Code-first analysis

Read for repeated model experiments, bulk diagnostics, extraction or token-cost work.
This changes execution shape, not the scientific depth or authorized scope.

## Split code from judgment

| Work | Owner |
| --- | --- |
| Fixed candidate/seed/fold loops, joins, hashes, coverage, metrics, intervals | Existing project runner or a small Python/R script |
| Hypothesis, legal features, time-safe validation, interpretation, promotion | Model plus independent scientific reviewer |
| Repeatable parsing/OCR | Installed extractor, content-hash cache, structural checks |
| Ambiguous text, diagrams, equations, failures | Model with bounded source spans/pages |

Look for the runner before writing one. A model per candidate is unnecessary when
the candidates differ only by configuration. Fan out judgment or genuinely distinct
implementation tracks, not seeds, rows or folds. If the user explicitly chooses a
different execution shape, preserve that choice and explain the cost tradeoff.

## Before execution

Freeze candidate configs, eligible rows, baseline, split/fold IDs, metric,
success rule and seeds in the existing experiment log. Validation and feature
selection stay inside the allowed training folds. Do not manufacture a new
holdout from years already inspected, or run extra fits to fill a usage window.

Code writes one record per attempted run, including failures. Record run ID,
config/data/code identity, fold IDs, denominators, baseline/candidate metrics,
warnings, runtime, exit status and artifact hashes. Reuse only completed,
validated outputs. Reuse also requires matching
data/code/config/environment and the frozen scientific contract: seeds, folds,
eligible row IDs/population, baseline, metric and validation charter. Changed
identity gets a new run. A partial file, exit zero or fresh mtime does not prove
a valid result.

Reuse the existing ledger/results schema. Do not build a framework or generic
job service for one analysis. Never overwrite frozen evidence to save tokens.

## Completion-driven handoff

- Use the runtime's task/job completion notification or blocking wait first.
  Record the exact job ID and log pointer once; keep one owner per job.
- While waiting, perform independent work when an already-authorized task is
  available; otherwise yield to the notification without inventing work.
  Do not wake a model just
  to repeat `tail`, status, elapsed-time narration or unchanged budget checks.
- If no notification/wait exists, poll in code with bounded backoff, deadline
  and terminal success/failure detection. A no-output interval alone is not a
  failure. Surface completion, explicit error or a diagnosed actionable stall.
- A wait deadline expiring leaves a live job pending; it is not an execution
  timeout or permission to kill/retry it. Record an execution timeout only when
  the runner reports one. Inspect the existing process before any retry; live
  jobs and real permission gates prohibit replacement work. Preserve checkpoint
  and actual reset policy.

Give the model the contract ID, compact metrics table, failed checks, unexpected
slices and artifact pointers, not the full data or repeated log history. Include
all candidates and denominators in machine output; summarize only what fits
without hiding failures. The reviewer can inspect full artifacts on demand.

## Cost evidence and quality gates

Measure a comparable task before and after: completed model turns, fresh input,
cache creation, cache reads, output, quality failures and runtime separately.
Deduplicate streaming messages by stable message ID before summing usage.
Raw cached tokens, transcript bytes and tool counts are not billed dollars or
subscription quota. Image base64 bytes are not text tokens. Do not promise a
savings percentage without matched outcome and usage evidence.

Use code for syntax, hashes, recounts and parity. Keep independent judgment for
scientific claims, leakage, uncertain extraction and user-facing conclusions.
Cheaper models are an evaluated routing choice, not a blanket downgrade. Do not
change permission modes, bypass guards or revive completed tasks for efficiency.
