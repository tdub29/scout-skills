# Setup and Sync

## Setup

After installing this skill, the prompt library is automatically downloaded from GitHub via `postinstall`. No credentials needed â€” all data is publicly available.

If references are missing, run manually:
```bash
node scripts/setup.js
```

**Keep references up to date** (GitHub syncs community prompts twice daily):
```bash
# Force pull latest references (recommended weekly)
pnpm run sync
# or equivalently
node scripts/setup.js --force
```

Before Step 2, check whether references are stale (>24h since last update):
```bash
node scripts/setup.js --check
```

This fetches the latest `references/*.json` files from:
https://github.com/YouMind-OpenLab/ai-image-prompts-skill/tree/main/references
