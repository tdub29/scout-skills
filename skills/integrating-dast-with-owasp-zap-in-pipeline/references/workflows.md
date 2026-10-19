# Workflow Reference: DAST with OWASP ZAP

## DAST Pipeline Integration

```
Build & Deploy to Staging
       â”‚
       â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ Health Check      â”‚
â”‚ (wait for ready)  â”‚
â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”˜
       â”‚
       â”œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
       â–¼              â–¼
â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”  â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
â”‚ ZAP       â”‚  â”‚ ZAP API   â”‚
â”‚ Baseline  â”‚  â”‚ Scan      â”‚
â”‚ Scan      â”‚  â”‚ (OpenAPI) â”‚
â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜  â””â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”˜
      â”‚               â”‚
      â””â”€â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
              â–¼
       â”Œâ”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”
       â”‚ Report Gen   â”‚
       â”‚ + Upload     â”‚
       â””â”€â”€â”€â”€â”€â”€â”¬â”€â”€â”€â”€â”€â”€â”€â”˜
              â”‚
       â”Œâ”€â”€â”€â”€â”€â”€â”´â”€â”€â”€â”€â”€â”€â”
       â–¼             â–¼
     PASS          FAIL
     Deploy to     Block +
     Production    Alert
```

## ZAP Scan Types Comparison

| Scan Type | Duration | Coverage | CI/CD Suitable | Active Attacks |
|-----------|----------|----------|----------------|----------------|
| Baseline | 2-5 min | Passive only | Yes | No |
| Full Scan | 30-120 min | Comprehensive | Scheduled | Yes |
| API Scan | 5-15 min | API endpoints | Yes | Yes |

## ZAP Docker Commands

```bash
# Baseline scan (passive)
docker run --rm -v $(pwd):/zap/wrk zaproxy/zap-stable \
  zap-baseline.py -t http://target:8080 \
  -r report.html -J report.json -c rules.tsv

# Full scan (active)
docker run --rm -v $(pwd):/zap/wrk zaproxy/zap-stable \
  zap-full-scan.py -t http://target:8080 \
  -r report.html -J report.json -c rules.tsv -T 60

# API scan (OpenAPI)
docker run --rm -v $(pwd):/zap/wrk zaproxy/zap-stable \
  zap-api-scan.py -t http://target:8080/openapi.json \
  -f openapi -r report.html -J report.json
```

## Authenticated Scanning Configuration

```yaml
# zap-auth-config.yaml
authentication:
  method: form
  loginUrl: http://target:8080/login
  parameters:
    username: testuser
    password: testpass123
  loggedInIndicator: "\\QWelcome\\E"
  loggedOutIndicator: "\\QSign In\\E"

context:
  name: "auth-context"
  include:
    - "http://target:8080/.*"
  exclude:
    - "http://target:8080/logout"
    - "http://target:8080/static/.*"
```
