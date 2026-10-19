

export function generateRepoModeSection(): string {
  return `## Repo Ownership â€” See Something, Say Something

\`REPO_MODE\` controls how to handle issues outside your branch:
- **\`solo\`** â€” You own everything. Investigate and offer to fix proactively.
- **\`collaborative\`** / **\`unknown\`** â€” Flag via AskUserQuestion, don't fix (may be someone else's).

Always flag anything that looks wrong â€” one sentence, what you noticed and its impact.`;
}

