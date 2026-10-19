---
name: firebase-migration
description: Guide for migrating from Prisma/NextAuth to Firebase. Use when the user says "migrate to Firebase", "Firebase migration", "convert to Firestore", or asks about Firebase setup.
---

# Firebase Migration Guide

This skill guides the migration from the current Prisma/NextAuth stack to Firebase (Auth, Firestore, Cloud Functions).

## Migration Overview

```
Current Stack                    Firebase Stack
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
NextAuth                    â†’    Firebase Auth
Prisma + SQLite/Postgres    â†’    Firestore
Next.js API Routes          â†’    Cloud Functions (optional)
middleware.ts               â†’    Firebase App Check + middleware
lib/db/*.ts                 â†’    lib/firebase/*.ts
```

## Pre-Migration Checklist

Before starting migration:

- [ ] Create Firebase project at console.firebase.google.com
- [ ] Enable Authentication (Email/Password provider)
- [ ] Create Firestore database
- [ ] Install Firebase CLI: `npm install -g firebase-tools`
- [ ] Login: `firebase login`
- [ ] Initialize project: `firebase init`

## Phase 1: Setup Firebase

Load `references/phase-1-setup.md` when installing dependencies, writing client and Admin SDK config, or setting env vars.

## Phase 2: Migrate Authentication

Load `references/phase-2-auth.md` when writing the auth context, auth functions, or server-side token verification.

## Phase 3: Migrate Data Layer

Load `references/phase-3-data-layer.md` when converting repository functions, mapping models, or designing the Firestore structure.

## Phase 4: Security Rules

Load `references/phase-4-security-rules.md` when writing or deploying firestore.rules.

## Phase 5: Data Migration

Load `references/phase-5-data-migration.md` when exporting from Prisma and importing to Firestore.

## Phase 6: Update Imports

### 6.1 Find and Replace

```bash
# Find all imports from lib/db
rg "from ['\"]@/lib/db['\"]" --type ts

# Update to lib/firebase
# In each file, change:
# import { ... } from "@/lib/db";
# to:
# import { ... } from "@/lib/firebase";
```

### 6.2 Update Auth Imports

```typescript
// Before
import { auth } from "@/auth";
const session = await auth();

// After
import { getServerSession } from "@/lib/firebase/server-auth";
const session = await getServerSession();
```

## Phase 7: Cleanup

After migration is complete and tested:

- [ ] Remove Prisma dependencies: `npm uninstall prisma @prisma/client`
- [ ] Delete `prisma/` folder
- [ ] Delete `lib/db/` folder
- [ ] Delete `lib/db.ts`
- [ ] Remove NextAuth: `npm uninstall next-auth`
- [ ] Delete `auth.ts`
- [ ] Update `.env.example` with Firebase variables
- [ ] Update README with new setup instructions

## Testing Checklist

- [ ] User registration works
- [ ] User login works
- [ ] User logout works
- [ ] Protected routes redirect to login
- [ ] Leagues CRUD operations work
- [ ] League membership works
- [ ] Lineup submission works
- [ ] Standings calculation works
- [ ] Security rules enforce permissions
- [ ] No Prisma errors in console

## Rollback Plan

If issues arise, the repository pattern allows quick rollback:

1. Change imports back: `from "@/lib/firebase"` â†’ `from "@/lib/db"`
2. Restore auth: `getServerSession` â†’ `auth()`
3. Re-enable Prisma dependencies

The consuming code doesn't change, only the import paths.

## References

- `references/phase-1-setup.md`: load in Phase 1 (install, client config, Admin SDK config, env vars)
- `references/phase-2-auth.md`: load in Phase 2 (auth context, auth functions, server-side verification)
- `references/phase-3-data-layer.md`: load in Phase 3 (repository conversion, data model mapping, Firestore structure)
- `references/phase-4-security-rules.md`: load in Phase 4 (firestore.rules and deploy)
- `references/phase-5-data-migration.md`: load in Phase 5 (Prisma export, Firestore import)
