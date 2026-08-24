# UNPS HiveForge v0.6.0 — Guided Onboarding

HiveForge v0.6.0 keeps the v0.5.0 production control plane and adds a complete guided user experience for both inexperienced users and experienced operators.

## Highlights

- guided discovery → install → intake → first verified task journey;
- `hiveforge onboard` copy/paste startup workflow;
- `hiveforge docs` documentation router;
- `hiveforge profile-init` human-readable working-profile template;
- `hiveforge project-init` optional project-intake template with overwrite protection;
- domain-specific Guided / Working / Expert interaction modes;
- recommended workflow and input guide;
- complete CLI command reference;
- Tool/capability maturity guide;
- optional ToolJet team-cockpit setup and Compose stack;
- README visualizations for architecture, learning, workflow lifecycle, and ToolJet boundaries;
- user-context-aware BRAIN with returning-user delta checks;
- production tests for onboarding CLI behavior and ToolJet Compose validation.

## User-context safety

HiveForge separates:

- user working preferences;
- client/project facts;
- current task state.

Reusable user context explicitly excludes passwords, API keys, tokens, private keys, auth cookies, regulated data, unrelated sensitive personal information, temporary emotional state, and one-off project exceptions.

## First run

```bash
HIVEFORGE_REF=v0.6.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.6.0/install.sh | sh

hiveforge doctor
hiveforge onboard
```

Optional:

```bash
hiveforge profile-init
hiveforge project-init
hiveforge dashboard
hiveforge tooljet status
```

## Core versus optional capabilities

The core package can be Production while optional capabilities retain independent maturity:

- Graphify — Candidate;
- yt-dlp — Candidate;
- Composio — Staged;
- LangGraph — Staged;
- ToolJet registry runtime — Staged.

Their absence must not break core HiveForge operation.

## Validation

The v0.6.0 Production Gate includes:

- package/version/status consistency;
- public/private and secret scanning;
- onboarding documentation integrity;
- onboarding/profile/project CLI smoke tests;
- Linux/macOS/WSL fresh installs;
- dashboard health smoke;
- Graphify 0.9.48 live extraction + clustering;
- fallback without Graphify;
- package export/import round trips;
- ToolJet Compose validation;
- v0.6.0 acceptance evidence.

Release archives include `SHA256SUMS` and are published from the exact tested `main` commit.
