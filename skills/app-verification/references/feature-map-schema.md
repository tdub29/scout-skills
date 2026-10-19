# `feature-map.json` schema

Lives at `<project>/.agents/feature-map.json`. Read by `.agents/scripts/verify-app.py`.

## Top level

| Key | Required | Meaning |
|---|---|---|
| `app` | yes | Short name, printed in the report |
| `entry` | yes | How to open the app (below) |
| `features` | yes | Array of features, each with a unique `id` |
| `setup` | no | Steps run once after first load, before any feature (dismiss a modal, seed localStorage) |
| `viewport` | no | `{width, height}`, default `1440x900` |
| `timeoutMs` | no | Per-action timeout, default `15000` |
| `failOnConsoleError` | no | Default `true`. Set `false` only for an app with known third-party noise, and say why in a comment field |

## `entry`

```jsonc
{ "type": "file", "path": "finances.html" }                  // standalone html, opened as file://

{ "type": "url", "url": "https://trevor-apps.pages.dev/x" }  // already-hosted

{ "type": "server",                                          // spawn a dev server, kill it after
  "cmd": "npm run dev -- --port {port}",
  "cwd": "web",
  "url": "http://127.0.0.1:{port}",                          // optional, this is the default
  "port": 5173,                                              // optional, omit to pick a free one
  "env": { "NODE_ENV": "development" },                      // optional
  "readyTimeout": 90 }                                       // seconds to wait for a response
```

`{port}` is substituted into `cmd`, `url`, and every value in `env` - plenty of servers take their
port from the environment rather than a flag, and a literal `{port}` there makes the server exit
before it binds. The server is killed tree-wide on exit, so a crashed run does not leave a port
held.

Pin `port` explicitly when the app hardcodes it somewhere the runner cannot reach: a Vite proxy
target, an `AUTH_URL` origin, a CORS allowlist. A free port would start the app and then fail
every request it makes to itself.

## A feature

```jsonc
{
  "id": "net-worth",              // required, unique, stable - this is the handle in --feature
  "name": "Net worth headline",   // human label for the report
  "path": ["#tab-overview"],      // steps to reach it from a fresh load (see below)
  "selector": "[data-verify=net-worth]",
  "expect": { "textMatches": "\\$[0-9,]+" },
  "assert": "document.querySelectorAll('.account-row').length > 3",  // JS, must be truthy
  "absent": ".error-banner",      // fails if this IS present
  "reload": true,                 // default true: reload before this feature so state is clean
  "viewport": {"width": 420, "height": 860},  // resize for THIS feature only, then restore
  "notes": "Cmd+1. Blank usually means the accounts JSON failed to parse."
}
```

Use `viewport` for a control that only exists at one width - a phone hamburger, a bottom tab bar,
a desktop-only sidebar. At the wrong width the element is `display:none`, Playwright refuses to
click it, and the feature reads as broken when it is only hidden. The map-level `viewport` is
restored after the feature runs.

At least one of `selector`, `assert`, or `absent` should be present, or the feature only proves the
click path did not throw.

### `path` steps

A bare string is shorthand for `{"click": "<selector>"}`.

| Step | Does |
|---|---|
| `{"click": "sel"}` | click |
| `{"fill": "sel", "value": "text"}` | type into an input |
| `{"select": "sel", "value": "opt"}` | choose a `<select>` option |
| `{"press": "Enter"}` | keyboard, Playwright key names |
| `{"waitFor": "sel"}` | wait for a selector |
| `{"eval": "js"}` | run JS in the page (seed state, stub a clock) |
| `{"sleepMs": 300}` | last resort - prefer `waitFor`, a sleep hides a race |

### `expect`

| Key | Checks |
|---|---|
| `textMatches` | regex against the element's inner text (JSON-escape your backslashes) |
| `minCount` | at least N elements match `selector` - catches an empty list that still renders |

## Selector hygiene

Prefer `[data-verify=<id>]` added to the app over a CSS-path or nth-child selector. A selector that
breaks when someone restyles a div produces false failures, and a check people learn to ignore is
worse than no check.

## What the runner captures regardless

Every run collects console `error`s, uncaught page exceptions, and failed network requests across
the whole session, with known noise (favicon, devtools, sourcemaps) filtered. With
`failOnConsoleError` on, any of them fails the run even if every feature passed - a page that
renders while throwing is not verified.
