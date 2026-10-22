# Optional Jev: setup and routing

Jev answers typed questions about supplied evidence. The local ranker stays offline. This
optional client is for bounded decisions during scouting or the task that follows it.

## Setup

Python 3.9+ is required by the bundled client. It uses only the standard library. Get your own
key from the [TypeSafe console](https://console.typesafe.ai/keys), then set `TYPESAFE_API_KEY`
in your local shell or secret manager. Never paste a real key into chat, commit it, or place it
in a shared prompt. The client does not read `.env` files or other projects' credentials.

PowerShell, with a placeholder only:

```powershell
$env:TYPESAFE_API_KEY = 'YOUR_LOCAL_KEY'
```

Bash, with a placeholder only:

```sh
export TYPESAFE_API_KEY='YOUR_LOCAL_KEY'
```

Use the script inside the installed scout-skills bundle, or this checkout:

```sh
python skills/scout-skills/scripts/jev.py --state "This excerpt gives keyboard focus rules for a dialog." --noul contributes="Does this excerpt give a concrete accessibility rule?" --dry-run
```

`--dry-run` validates inputs and prints the first exact payload plus the batch count without
a key or network access. Omit it only after confirming permission to send that state and use
the account's API. That request sends state, questions, model ID and authentication to
`https://api.typesafe.ai/v1/systemone`. The local search command sends nothing.

Do not assume Jev is free. Check the account's current terms and
[model pricing](https://docs.typesafe.ai/models) before enabling it. This package grants no
standing spending or data-sharing authorization. Keep credentials and private third-party data
out of state. A user's existing standing authorization applies within its actual scope.

## Choose the right phase

| Work | Route |
|---|---|
| Read files, search descriptions/bodies, count or join rows | Local code |
| Exact validation or known regex match | Local code |
| Generate instructions, research sources, explain findings | Agent |
| Judge whether collected excerpts contribute to a named sub-question | Optional Jev `noul` |
| Select among known routes using supplied evidence | Optional Jev `choice` |
| Rate an item against ordered descriptions | Optional Jev `score` |

Use Jev when the judgment is bounded, the evidence is already in hand, and moving a repeated
phase out of the agent is useful. A single obvious decision needs no extra API call. Broad
research, missing evidence and final source verification stay with the agent. One selected lead
does not remove other contributors. A low relevance judgment is a review signal, not grounds
to discard an unread skill.

## Single items and batches

```sh
python skills/scout-skills/scripts/jev.py --state "The task is to debug a failing build." --choice route="Which phase is needed?" --option research="Find missing evidence" --option generation="Write a fix" --option validation="Check supplied output"
python skills/scout-skills/scripts/jev.py --state-jsonl items.jsonl --field text --noul contributes="Does this excerpt contain concrete guidance for keyboard accessibility?" --workers 4
python skills/scout-skills/scripts/jev.py --state-jsonl items.jsonl --field text --score relevance="How directly does this excerpt address keyboard accessibility?" --level unrelated --level adjacent --level direct --dry-run
```

Each nonblank input line must be a JSON object, for example
`{"id":"dialog-focus","text":"Move focus into the dialog when it opens."}`.
`--id-field` defaults to `id`; `--field` selects state, otherwise the entire object is sent.
Missing fields and invalid/empty batches fail before any request. Every attempted item produces
one JSONL row in input order, including failures, with `_id`, `_model`, `_usage`, and either
typed answer fields or `_error`. Any failed item makes the command exit 1. Input/key errors
exit 2. An empty batch is an input error, never success.

`noul` is a probability of yes, not a Boolean. Choice and score retain probabilities and
confidence. Choose thresholds using labeled examples for your task; review uncertain rows.
Do not interpret generic confidence as a calibrated guarantee for your labels. Keep counts
and joins in code, check input/output reconciliation, and never silently drop failed items.

The default is pinned to `jev-1.13.0`. Override explicitly with `--model` or `JEV_MODEL`, and
revalidate thresholds when changing it. Transport errors, rate limits and server errors get
bounded retries; authentication and validation failures are not retried. The client never
truncates evidence. Server context limits still apply; split oversized evidence deliberately.

## Sources and maintenance

API contract and model pin verified against TypeSafe documentation on 2026-10-22:
[System One API](https://docs.typesafe.ai/api/system-one),
[models](https://docs.typesafe.ai/models),
[confidence](https://docs.typesafe.ai/confidence), and
[coding agents](https://docs.typesafe.ai/introduction/coding-agents).
The routing table and conservative review policy are this project's operating choices.
They are not a promise of accuracy, speed, savings or provider pricing.
