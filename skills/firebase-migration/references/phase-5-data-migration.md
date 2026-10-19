# Phase 5: Data Migration

## Phase 5: Data Migration

### 5.1 Export from Prisma

```typescript
// scripts/export-data.ts
import { prisma } from "@/lib/db";
import fs from "fs";

async function exportData() {
  const users = await prisma.user.findMany();
  const leagues = await prisma.league.findMany();
  const members = await prisma.leagueMember.findMany();
  const tournaments = await prisma.tournament.findMany();
  const golfers = await prisma.golfer.findMany();
  const lineups = await prisma.lineup.findMany({
    include: { golfers: true },
  });

  fs.writeFileSync("export.json", JSON.stringify({
    users, leagues, members, tournaments, golfers, lineups
  }, null, 2));
}

exportData();
```

### 5.2 Import to Firestore

```typescript
// scripts/import-to-firestore.ts
import { adminDb } from "@/lib/firebase-admin";
import data from "./export.json";

async function importData() {
  const batch = adminDb.batch();

  // Users
  for (const user of data.users) {
    const ref = adminDb.collection("users").doc(user.id);
    batch.set(ref, {
      email: user.email,
      name: user.name,
      createdAt: new Date(user.createdAt),
    });
  }

  // Leagues
  for (const league of data.leagues) {
    const ref = adminDb.collection("leagues").doc(league.id);
    batch.set(ref, {
      name: league.name,
      type: league.type,
      inviteCode: league.inviteCode,
      createdById: league.createdById,
      createdAt: new Date(league.createdAt),
    });
  }

  // ... continue for other collections

  await batch.commit();
  console.log("Migration complete");
}

importData();
```
