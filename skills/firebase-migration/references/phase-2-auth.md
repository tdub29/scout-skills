# Phase 2: Migrate Authentication

## Phase 2: Migrate Authentication

### 2.1 Create Auth Context

```typescript
// components/providers/AuthProvider.tsx
"use client";

import { createContext, useContext, useEffect, useState } from "react";
import { User, onAuthStateChanged } from "firebase/auth";
import { auth } from "@/lib/firebase";

type AuthContextType = {
  user: User | null;
  loading: boolean;
};

const AuthContext = createContext<AuthContextType>({ user: null, loading: true });

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    return onAuthStateChanged(auth, (user) => {
      setUser(user);
      setLoading(false);
    });
  }, []);

  return (
    <AuthContext.Provider value={{ user, loading }}>
      {children}
    </AuthContext.Provider>
  );
}

export const useAuth = () => useContext(AuthContext);
```

### 2.2 Create Auth Functions

```typescript
// lib/firebase/auth.ts
import {
  createUserWithEmailAndPassword,
  signInWithEmailAndPassword,
  signOut as firebaseSignOut,
} from "firebase/auth";
import { auth } from "@/lib/firebase";

export async function signUp(email: string, password: string) {
  const credential = await createUserWithEmailAndPassword(auth, email, password);
  return credential.user;
}

export async function signIn(email: string, password: string) {
  const credential = await signInWithEmailAndPassword(auth, email, password);
  return credential.user;
}

export async function signOut() {
  await firebaseSignOut(auth);
}
```

### 2.3 Server-side Auth Verification

```typescript
// lib/firebase/server-auth.ts
import { cookies } from "next/headers";
import { adminAuth } from "@/lib/firebase-admin";

export async function getServerSession() {
  const cookieStore = cookies();
  const token = cookieStore.get("firebase-token")?.value;

  if (!token) return null;

  try {
    const decoded = await adminAuth.verifyIdToken(token);
    return { user: { id: decoded.uid, email: decoded.email } };
  } catch {
    return null;
  }
}
```
