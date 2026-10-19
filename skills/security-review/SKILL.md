---
name: security-review
description: "Auth, secrets, input handling. OWASP checklist"
---

# Security Review Skill

This skill ensures all code follows security best practices and identifies potential vulnerabilities.

## When to Activate

- Implementing authentication or authorization
- Handling user input or file uploads
- Creating new API endpoints
- Working with secrets or credentials
- Implementing payment features
- Storing or transmitting sensitive data
- Integrating third-party APIs

## Security Checklist

### 1. Secrets Management

#### âŒ NEVER Do This
```typescript
const apiKey = "sk-proj-xxxxx"  // Hardcoded secret
const dbPassword = "password123" // In source code
```

#### âœ… ALWAYS Do This
```typescript
const apiKey = process.env.OPENAI_API_KEY
const dbUrl = process.env.DATABASE_URL

// Verify secrets exist
if (!apiKey) {
  throw new Error('OPENAI_API_KEY not configured')
}
```

#### Verification Steps
- [ ] No hardcoded API keys, tokens, or passwords
- [ ] All secrets in environment variables
- [ ] `.env.local` in .gitignore
- [ ] No secrets in git history
- [ ] Production secrets in hosting platform (Vercel, Railway)

### 2. Input Validation

#### Always Validate User Input
```typescript
import { z } from 'zod'

const CreateUserSchema = z.object({
  email: z.string().email(),
  name: z.string().min(1).max(100),
  age: z.number().int().min(0).max(150)
})

export async function createUser(input: unknown) {
  try {
    const validated = CreateUserSchema.parse(input)
    return await db.users.create(validated)
  } catch (error) {
    if (error instanceof z.ZodError) {
      return { success: false, errors: error.errors }
    }
    throw error
  }
}
```

#### File Upload Validation
```typescript
function validateFileUpload(file: File) {
  const maxSize = 5 * 1024 * 1024
  if (file.size > maxSize) throw new Error('File too large (max 5MB)')

  const allowedTypes = ['image/jpeg', 'image/png', 'image/gif']
  if (!allowedTypes.includes(file.type)) throw new Error('Invalid file type')

  const allowedExtensions = ['.jpg', '.jpeg', '.png', '.gif']
  const extension = file.name.toLowerCase().match(/\.[^.]+$/)?.[0]
  if (!extension || !allowedExtensions.includes(extension)) throw new Error('Invalid file extension')

  return true
}
```

#### Verification Steps
- [ ] All user inputs validated with schemas
- [ ] File uploads restricted (size, type, extension)
- [ ] No direct use of user input in queries
- [ ] Whitelist validation (not blacklist)
- [ ] Error messages don't leak sensitive info

### 3. SQL Injection Prevention

#### âŒ NEVER Concatenate SQL
```typescript
const query = `SELECT * FROM users WHERE email = '${userEmail}'`
await db.query(query)
```

#### âœ… ALWAYS Use Parameterized Queries
```typescript
const { data } = await supabase.from('users').select('*').eq('email', userEmail)
// Or: await db.query('SELECT * FROM users WHERE email = $1', [userEmail])
```

#### Verification Steps
- [ ] All database queries use parameterized queries
- [ ] No string concatenation in SQL
- [ ] ORM/query builder used correctly

### 4. Authentication & Authorization

#### JWT Token Handling
```typescript
// âŒ WRONG: localStorage (vulnerable to XSS)
localStorage.setItem('token', token)

// âœ… CORRECT: httpOnly cookies
res.setHeader('Set-Cookie',
  `token=${token}; HttpOnly; Secure; SameSite=Strict; Max-Age=3600`)
```

#### Authorization Checks
- [ ] Tokens stored in httpOnly cookies (not localStorage)
- [ ] Authorization checks before sensitive operations
- [ ] Row Level Security enabled (Supabase/Firestore)
- [ ] Role-based access control implemented

### 5. XSS Prevention

- [ ] User-provided HTML sanitized (e.g. DOMPurify)
- [ ] CSP headers configured
- [ ] No unvalidated dynamic content rendering

### 6. CSRF Protection

- [ ] CSRF tokens on state-changing operations
- [ ] SameSite=Strict on all cookies
- [ ] Double-submit cookie pattern for forms

### 7. Rate Limiting

- [ ] Rate limiting on all API endpoints
- [ ] Stricter limits on expensive operations (search, auth)
- [ ] IP-based and user-based limits

### 8. Sensitive Data Exposure

- [ ] No passwords, tokens, or secrets in logs
- [ ] Error messages generic for users (no stack traces)
- [ ] Detailed errors only in server logs

### 9. Dependency Security

```bash
npm audit
npm audit fix
npm outdated
```

- [ ] Dependencies up to date
- [ ] No known vulnerabilities (npm audit clean)
- [ ] Lock files committed
- [ ] Dependabot enabled

## Pre-Deployment Security Checklist

- [ ] **Secrets**: No hardcoded secrets, all in env vars
- [ ] **Input Validation**: All user inputs validated
- [ ] **SQL Injection**: All queries parameterized
- [ ] **XSS**: User content sanitized
- [ ] **CSRF**: Protection enabled
- [ ] **Authentication**: Proper token handling
- [ ] **Authorization**: Role checks in place
- [ ] **Rate Limiting**: Enabled on all endpoints
- [ ] **HTTPS**: Enforced in production
- [ ] **Security Headers**: CSP, X-Frame-Options configured
- [ ] **Error Handling**: No sensitive data in errors
- [ ] **Logging**: No sensitive data logged
- [ ] **Dependencies**: Up to date, no vulnerabilities

## Resources

- [references/cloud-infrastructure-security.md](references/cloud-infrastructure-security.md): IAM, cloud secrets, CI/CD pipeline security, infrastructure-as-code, CDN/edge, and disaster recovery for AWS, Vercel, Railway, and Cloudflare. The layer above this checklist's app-level scope.
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Next.js Security](https://nextjs.org/docs/security)
- [Web Security Academy](https://portswigger.net/web-security)
- Project: `_/docs/security/security-reviewer.md` (workflow + scan commands)
- Project: `SECURITY_PRD.md` (pre-launch requirements)

---

**Remember**: Security is not optional. One vulnerability can compromise the entire platform. When in doubt, err on the side of caution.
