# Cloud Infrastructure Security

Covers the deployment-platform layer the main checklist doesn't: IAM, secrets at the platform level, CI/CD, infrastructure-as-code, CDN/edge, and disaster recovery. Scoped to the stacks this workspace actually deploys to (AWS, Vercel, Railway, Cloudflare).

## 1. IAM and Least Privilege

#### âŒ NEVER Do This
```json
{
  "Effect": "Allow",
  "Action": "*",
  "Resource": "*"
}
```

#### âœ… ALWAYS Do This
```json
{
  "Effect": "Allow",
  "Action": ["s3:GetObject", "s3:PutObject"],
  "Resource": "arn:aws:s3:::my-bucket/uploads/*"
}
```

#### Verification Steps
- [ ] No `"Action": "*"` or `"Resource": "*"` on any role a deployed service assumes
- [ ] MFA required on every human account with console access; service accounts use short-lived roles, not long-lived keys
- [ ] Each service's role grants only the actions and resources that service actually calls, not the account's full permission set

## 2. Cloud Secrets Management

#### Verification Steps
- [ ] Secrets live in the platform's own secrets store (AWS Secrets Manager/SSM Parameter Store, Vercel/Railway environment variables), not the main checklist's `.env.local` alone for anything deployed
- [ ] Secrets are scoped per environment (prod secret never present in a preview/staging deploy)
- [ ] A rotation path exists for every credential that can be rotated (DB password, API key), even if rotation is manual today

## 3. CI/CD Pipeline Security

#### Verification Steps
- [ ] CI authenticates to cloud providers via OIDC federation, not a long-lived access key pasted into repo secrets
- [ ] Dependency and secret scanning run on every PR (`npm audit`, a secret-scanner step), not just locally before a release
- [ ] A deploy workflow cannot be triggered from a fork's pull request without a maintainer approval gate

## 4. Infrastructure as Code

#### Verification Steps
- [ ] Infra changes (Terraform/CDK/Pulumi, or platform config) go through the same PR review as application code, not a console click
- [ ] State files are never committed to the repo and never hold plaintext secrets
- [ ] A `plan`/diff step runs before `apply` in CI, so a reviewer sees what will change before it changes

## 5. CDN / Edge Security

#### Verification Steps
- [ ] Security headers (CSP, `X-Frame-Options`, `Strict-Transport-Security`) are set at the CDN/edge layer (Cloudflare, Vercel headers config), not only hoped-for from the app
- [ ] A WAF or rate-limiting rule sits in front of any public API route, in addition to the app-level rate limiting from the main checklist
- [ ] Origin access is restricted to the CDN (origin doesn't answer direct requests that skip Cloudflare/Vercel's edge)

## 6. Backup and Disaster Recovery

#### Verification Steps
- [ ] Automated backups are enabled on every production database, with a tested restore, not just "backups are on"
- [ ] RPO (how much data you can lose) and RTO (how long recovery takes) are written down for at least the primary database, even as a rough number
- [ ] A restore has actually been run once against a non-production target; an untested backup is a hope, not a plan

## Common Cloud Misconfigurations

- **Public S3 bucket or storage container** holding anything other than intentionally public assets. Check bucket policy AND account-level public-access block together, one can override the other.
- **Publicly accessible RDS/managed database** with no security-group restriction to the app's own VPC/network.
- **A preview/staging deploy pointed at the production database** because an environment variable was copied instead of scoped.
