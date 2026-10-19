# Phase 4: Security Rules

## Phase 4: Security Rules

### 4.1 Create firestore.rules

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {

    // Users - only own data
    match /users/{userId} {
      allow read: if request.auth != null && request.auth.uid == userId;
      allow create: if request.auth != null && request.auth.uid == userId;
      allow update: if request.auth != null && request.auth.uid == userId;
      allow delete: if false;
    }

    // Leagues - members can read, admins can write
    match /leagues/{leagueId} {
      allow read: if request.auth != null && isMember(leagueId);
      allow create: if request.auth != null;
      allow update, delete: if request.auth != null && isAdmin(leagueId);
    }

    // League members
    match /leagueMembers/{docId} {
      allow read: if request.auth != null;
      allow create: if request.auth != null;
      allow update, delete: if request.auth != null &&
        isAdmin(resource.data.leagueId);
    }

    // Lineups - users can only manage their own
    match /lineups/{lineupId} {
      allow read: if request.auth != null;
      allow create: if request.auth != null &&
        request.resource.data.userId == request.auth.uid;
      allow update: if request.auth != null &&
        resource.data.userId == request.auth.uid;
      allow delete: if false;
    }

    // Tournaments & Golfers - read-only for authenticated users
    match /tournaments/{docId} {
      allow read: if request.auth != null;
      allow write: if false; // Admin SDK only
    }

    match /golfers/{docId} {
      allow read: if request.auth != null;
      allow write: if false; // Admin SDK only
    }

    // Helper functions
    function isMember(leagueId) {
      return exists(/databases/$(database)/documents/leagueMembers/$(leagueId)_$(request.auth.uid));
    }

    function isAdmin(leagueId) {
      return get(/databases/$(database)/documents/leagueMembers/$(leagueId)_$(request.auth.uid)).data.role == 'ADMIN';
    }
  }
}
```

### 4.2 Deploy Rules

```bash
firebase deploy --only firestore:rules
```
