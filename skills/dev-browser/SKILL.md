---
name: dev-browser
description: "Browser automation that keeps page state per call"
---

# Dev Browser

A CLI for controlling browsers with sandboxed JavaScript scripts.

## Installation

```bash
npm install -g dev-browser
dev-browser install
```

## Usage

Run `dev-browser --help` to learn more.

Named daemon-launched browsers persist by default. For unattended work, `--idle-timeout 5m` closes each launched browser after inactivity while preserving its profile and login state. The setting never closes Chrome attached with `--connect`; use `--idle-timeout 0` to disable configured cleanup.
