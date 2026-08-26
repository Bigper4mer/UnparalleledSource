# UNPS HiveForge v0.7.0 — Agent Operations

HiveForge v0.7.0 turns the portable control plane into a traceable agent-operations workflow while preserving the public/private boundary.

## Highlights

- Goal and multi-source intake with an execution plan before work begins.
- Explicit routing across skills, tools, connectors, MCPs, models, and harnesses.
- Local run identifiers, heartbeat telemetry, progress events, approvals, completion state, and connector health.
- Copy-ready deliverables with verification status and remaining limitations.
- Updated onboarding, manifests, Command Center versioning, and release evidence.

## Public package boundary

This release publishes reusable framework code, local runtime behavior, workflow contracts, documentation, tests, and safe examples. It does not publish private hosted-environment configuration, company user profiles, client or pursuit records, correspondence, connector exports, access tokens, API keys, or service-role credentials.

## Approval boundary

Research, analysis, drafting, and reversible local preparation may run inside the approved scope. External communications, submissions, pricing, legal commitments, credential changes, publishing outside this release, and other consequential writes remain human-approved actions.

## Install

```bash
HIVEFORGE_REF=v0.7.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.7.0/install.sh | sh
```

Release archives include `SHA256SUMS` and are built from the exact commit that passes the public Production Gate.
