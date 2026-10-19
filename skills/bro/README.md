<div align="center">

# ðŸ¤™ /bro

**When the answer made you go "bro what" â€” type `/bro` and get it in plain language.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Format: Agent Skills](https://img.shields.io/badge/format-Agent%20Skills-blue)](https://agentskills.io)
[![Works with](https://img.shields.io/badge/works%20with-Hermes%20%C2%B7%20Claude%20Code%20%C2%B7%20Cursor%20%C2%B7%20Codex%20%C2%B7%20opencode-blueviolet)](#compatibility)

</div>

---

## What is this?

`/bro` is a tiny [Agent Skills](https://agentskills.io)-format skill with one job: when the assistant's last reply was too dense, too jargon-heavy, or too formal, you type `/bro` and it re-explains **its own previous message** like a smart friend over a beer.

No new information. No new answers. Just the same thing, said in a way that's impossible to misunderstand.

It's one markdown file. The whole skill is [`SKILL.md`](SKILL.md).

## Compatibility

Works with any agent that reads the Agent Skills format â€” and ships thin slash-command wrappers where a skill alone doesn't give you a typed `/bro`:

| Tool | Skill location | Typed `/bro` via |
|---|---|---|
| **Hermes Agent** | `~/.hermes/skills/bro/SKILL.md` | skill (auto) |
| **Claude Code** | `~/.claude/skills/bro/SKILL.md` | `~/.claude/commands/bro.md` |
| **Cursor** | `~/.cursor/skills/bro/SKILL.md` | skill (`/bro`) |
| **OpenAI Codex** | `~/.codex/skills/bro/SKILL.md` | `~/.codex/prompts/bro.md` |
| **opencode** | `~/.config/opencode/skills/bro/SKILL.md` | `~/.config/opencode/command(s)/bro.md` |

Cursor also reads `~/.codex/skills/` and `~/.claude/skills/` (and the matching project folders) as a compatibility fallback. Don't rely on that â€” Cursor-only machines often have neither directory. The installer writes `~/.cursor/skills/bro/` whenever it detects Cursor, creating `~/.cursor/skills/` if needed (that folder is not there by default).

## Install

**One-liner** â€” detects which tools you have and installs into each:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/luchasarie/bro-skill/main/install.sh)
```

**Or from a clone** (better if you want to pull updates later):

```bash
git clone https://github.com/luchasarie/bro-skill.git
cd bro-skill
./install.sh          # installs into every detected tool
./install.sh --all    # or force-install into every supported tool
```

Then restart your agent session and type `/bro` after any reply that made your eyes glaze over.

## Update

```bash
cd bro-skill && git pull && ./install.sh
```

(Or just re-run the one-liner â€” it's idempotent.)

## Examples

**ðŸ§± Software architecture**

> The refactor introduces an idempotent reconciliation layer atop the event-sourced aggregate, thereby mitigating dual-write anomalies during the migration window while preserving backward compatibility with the legacy projection contract.

**`/bro`**

> Ok so basically: we added a safety layer that makes sure old and new data don't get out of sync while we're switching systems. Nothing breaks for anything still using the old system. That's it.

**â˜¸ï¸ Kubernetes panic**

> The CrashLoopBackOff stems from the liveness probe's failure threshold being exceeded due to the application's blocking initialization sequence, which starves the kubelet's health-check endpoint of a timely responseâ€¦

**`/bro`**

> Bro, your app takes too long to start up. Kubernetes keeps asking "you alive?" and your app is too busy booting to answer, so k8s kills it and restarts it â€” over and over. Give it more time (`initialDelaySeconds`) or move the slow startup work into an init container.

**ðŸ‡§ðŸ‡· Same-language rule â€” PT-BR in, PT-BR out**

> A otimizaÃ§Ã£o do funil de conversÃ£o demanda a implementaÃ§Ã£o de uma estratÃ©gia omnichannel de nurturing, visando a maximizaÃ§Ã£o do LTV atravÃ©s da reduÃ§Ã£o do churnâ€¦

**`/bro`**

> Mano, traduzindo: a gente quer que o cliente compre mais e fique mais tempo. Menos cliente indo embora + cada um gastando mais = mais dinheiro. Era isso que aquela sopa de sigla queria dizer.

**More in [`examples/`](examples/):** [git panic](examples/git-panic.md) (watch the commands survive verbatim), [consultant-speak](examples/consultant-speak.md), [full Kubernetes exchange](examples/kubernetes.md), [full architecture exchange](examples/software-architecture.md).

## The rules baked in

| Rule | What it means |
|---|---|
| ðŸ”„ **Re-explain, don't re-answer** | Never answers a new question, never adds info, never calls tools |
| ðŸ“ **Simpler, not shorter** | Clarity over word count â€” take the space real clarity needs |
| ðŸ“Œ **Facts survive verbatim** | Every path, command, filename, number, URL stays *exactly* the same |
| ðŸ¤™ **Light bro flavor** | Casual and direct, not a meme |
| ðŸŒ **Same language** | PT-BR in â†’ PT-BR out. English stays English |
| ðŸ§¹ **Flatten structure** | Headers and tables become plain sentences |

## File layout

```
bro-skill/
â”œâ”€â”€ SKILL.md     # the entire skill â€” one file, that's the beauty
â”œâ”€â”€ install.sh   # detects your agent CLIs and drops /bro into each
â”œâ”€â”€ examples/    # before/after pairs across domains and languages
â”œâ”€â”€ README.md    # you are here
â””â”€â”€ LICENSE      # MIT
```

## Contributing

It's a 30-line prompt file. If you have a genuinely better phrasing, open a PR â€” keep the facts-verbatim rule sacred.

## License

[MIT](LICENSE)
