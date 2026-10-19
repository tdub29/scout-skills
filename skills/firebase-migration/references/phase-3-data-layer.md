# Phase 3: Migrate Data Layer

## Contents

- [Phase 3: Migrate Data Layer](#phase-3-migrate-data-layer)
  - [3.1 Create Firestore Repository Structure](#31-create-firestore-repository-structure)
  - [3.2 Convert Repository Functions](#32-convert-repository-functions)
  - [3.3 Data Model Mapping](#33-data-model-mapping)
  - [3.4 Firestore Data Structure](#34-firestore-data-structure)

## Phase 3: Migrate Data Layer

### 3.1 Create Firestore Repository Structure

```
lib/
  firebase/
    index.ts      # Re-exports
    types.ts      # Copy from lib/db/types.ts (same types)
    users.ts
    leagues.ts
    tournaments.ts
    lineups.ts
    golfers.ts
    standings.ts
```

### 3.2 Convert Repository Functions

**Original (Prisma):**
```typescript
// lib/db/leagues.ts
export async function getLeague(id: string): Promise<League | null> {
  return prisma.league.findUnique({ where: { id } });
}

export async function createLeague(input: CreateLeagueInput): Promise<League> {
  return prisma.league.create({ data: input });
}

export async function getLeaguesForUser(userId: string): Promise<LeagueMembership[]> {
  return prisma.leagueMember.findMany({
    where: { userId },
    include: { league: true },
  });
}
```

**Converted (Firestore):**
```typescript
// lib/firebase/leagues.ts
import { db } from "@/lib/firebase";
import {
  collection,
  doc,
  getDoc,
  getDocs,
  addDoc,
  query,
  where,
  serverTimestamp,
} from "firebase/firestore";
import type { League, CreateLeagueInput, LeagueMembership } from "./types";

export async function getLeague(id: string): Promise<League | null> {
  const docRef = doc(db, "leagues", id);
  const docSnap = await getDoc(docRef);
  if (!docSnap.exists()) return null;
  return { id: docSnap.id, ...docSnap.data() } as League;
}

export async function createLeague(input: CreateLeagueInput): Promise<League> {
  const docRef = await addDoc(collection(db, "leagues"), {
    ...input,
    createdAt: serverTimestamp(),
  });
  return { id: docRef.id, ...input } as League;
}

export async function getLeaguesForUser(userId: string): Promise<LeagueMembership[]> {
  const q = query(
    collection(db, "leagueMembers"),
    where("userId", "==", userId)
  );
  const snap = await getDocs(q);

  const memberships: LeagueMembership[] = [];
  for (const memberDoc of snap.docs) {
    const memberData = memberDoc.data();
    const league = await getLeague(memberData.leagueId);
    if (league) {
      memberships.push({
        ...memberData,
        league,
      } as LeagueMembership);
    }
  }
  return memberships;
}
```

### 3.3 Data Model Mapping

| Prisma | Firestore |
|--------|-----------|
| Tables | Collections |
| Rows | Documents |
| Foreign keys | Document references or denormalized data |
| Joins | Multiple queries or denormalization |
| Transactions | `runTransaction()` |

### 3.4 Firestore Data Structure

```
firestore/
  users/
    {userId}/
      email: string
      name: string
      createdAt: timestamp

  leagues/
    {leagueId}/
      name: string
      type: "SINGLE" | "SEASON"
      inviteCode: string
      createdById: string
      createdAt: timestamp

  leagueMembers/
    {leagueId}_{userId}/   # Composite key for uniqueness
      leagueId: string
      userId: string
      role: "ADMIN" | "MEMBER"
      joinedAt: timestamp

  tournaments/
    {tournamentId}/
      externalId: string | null
      name: string
      startDate: timestamp
      endDate: timestamp
      status: "UPCOMING" | "IN_PROGRESS" | "COMPLETED"

  lineups/
    {lineupId}/
      leagueTournamentId: string
      userId: string
      golferIds: string[]
      createdAt: timestamp
      updatedAt: timestamp

  golfers/
    {golferId}/
      externalId: string
      name: string
      price: number
      ranking: number | null
```
