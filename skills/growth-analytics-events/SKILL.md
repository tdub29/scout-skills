---
name: growth-analytics-events
description: Define and instrument product analytics events for funnel, activation, and conversion tracking. Use when adding frontend/backend event schema, event naming, and measurement consistency.
---

Enforce a single event schema:
- event_name
- user_id
- session_id
- page
- cta_id
- report_id
- workspace_id
- timestamp
- meta

Ensure every CTA and lifecycle milestone emits one event with consistent naming.

Check:
1. Event names use snake_case.
2. Session ID is present.
3. Events never block user workflow on failure.

Use references/event-taxonomy.md.
