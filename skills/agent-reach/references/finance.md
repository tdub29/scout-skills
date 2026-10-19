# Market Data

Xueqiu stock quotes, search, and trending content. Quotes may be delayed and are not investment advice.

## Check status first

```bash
agent-reach doctor --json
```

When `xueqiu.active_backend` has a value, use that backend; a value of `null` only means Doctor did not
complete live content verification. Xueqiu needs a logged-in session or a minimal cookie, so never read an HTTP 400 as the stock not existing.

## OpenCLI (preferred when the desktop Chrome session is already logged in)

```bash
# Verify the current login session
opencli xueqiu whoami -f yaml

# Stock search and live quotes
opencli xueqiu search "è‹±ä¼Ÿè¾¾" -f yaml
opencli xueqiu stock NVDA -f yaml

# Trending content and trending stocks
opencli xueqiu hot -f yaml
opencli xueqiu hot-stock -f yaml

# List every read-only command
opencli xueqiu --help
```

OpenCLI only reuses a browser session the user already has and explicitly controls. Do not run
`opencli xueqiu login` automatically; when there is no existing session, have the user log in through Chrome first, or explicitly import
the minimal cookie Xueqiu needs:

```bash
agent-reach configure --from-browser chrome --platform xueqiu
```

That command reads and stores only `xq_a_token`; it does not collect cookies for any other platform along the way.

## Acceptance and failure handling

- Success means a stock name, ticker, price, or non-empty content list came back; exit code 0 with empty fields is not success.
- An HTTP 400 is usually a session or cookie problem, not a sign that the ticker does not exist.
- When `whoami` succeeds but `stock`/`hot` fails, report it as an adapter-parsing or platform-API problem; do not misdiagnose it as being logged out.
