# caveman-review

One-line PR comments. Location, problem, fix. No throat-clearing.

## What it does

Generates code review comments in `L<line>: <severity> <problem>. <fix>.` format. One line per finding. Severity emoji: ðŸ”´ bug, ðŸŸ¡ risk, ðŸ”µ nit, â“ question. Drops "I noticed that...", hedging, and restating what the diff already shows. Keeps exact line numbers, backticked symbols, and concrete fixes.

Auto-clarity: drops terse mode for CVE-class security findings, architectural disagreements, and onboarding contexts where the author needs the *why*. Resumes terse for the rest.

Output only â€” does not approve, request changes, or run linters.

## How to invoke

```
/caveman-review
```

Also triggers on "review this PR", "code review", "review the diff".

## Example output

```
L42: ðŸ”´ bug: user can be null after .find(). Add guard before .email.
L88-140: ðŸ”µ nit: 50-line fn does 4 things. Extract validate/normalize/persist.
L23: ðŸŸ¡ risk: no retry on 429. Wrap in withBackoff(3).
L107: â“ q: why drop the cache here? Reads on next request will miss.
```

## See also

- [`SKILL.md`](./SKILL.md) â€” full LLM-facing instructions
- [Caveman README](../../README.md) â€” repo overview
