# UNPS HiveForge v0.5.0

HiveForge v0.5.0 productionizes the portable agent-control package and adds a guided user journey for both inexperienced users and experienced operators without turning optional integrations into mandatory runtime dependencies.

## Highlights

- synchronized package/BRAIN Production release metadata;
- production CI gate and secret/public-private scans;
- fresh-install coverage for Linux, macOS and WSL/Ubuntu;
- dashboard health smoke testing;
- live Graphify fixture extraction/clustering plus Graphify-absent fallback testing;
- package export/import round trip;
- dependency maturity registry;
- staged Composio and LangGraph profiles;
- ToolJet Agent & Capability Registry contract;
- yt-dlp preferred media-ingestion policy;
- immutable release artifact with SHA-256 checksum;
- beginner-to-expert Getting Started guide;
- startup user-intake and scoped learning workflow;
- recommended workflow/input catalog;
- complete HiveForge command reference;
- tooling and capability-maturity guide;
- ToolJet setup/registry deployment guide;
- first-run copy/paste prompt;
- human-readable user-profile and project-intake templates;
- troubleshooting guide;
- expanded GitHub Mermaid visualizations for the user journey, architecture, workflow lifecycle and learning loop.

## First-time user path

```text
install
→ hiveforge doctor
→ hiveforge bootstrap
→ startup intake
→ inspect project/source of truth
→ recommend workflow
→ execute one real task
→ verify
→ capture validated learning
```

Start with [`docs/GETTING_STARTED.md`](GETTING_STARTED.md).

## Core versus optional capabilities

The HiveForge core package can be Production while optional capabilities retain independent maturity:

- Graphify — Candidate;
- yt-dlp — Candidate;
- Only-CLI — Candidate;
- Composio — Staged;
- LangGraph — Staged;
- ToolJet registry runtime — Staged.

Their absence must not break core HiveForge operation.

## Installation

```bash
HIVEFORGE_REF=v0.5.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.5.0/install.sh | sh

hiveforge doctor
hiveforge version
hiveforge bootstrap
```

For downloaded release archives, verify `SHA256SUMS` before use.

## First-run prompt

After bootstrapping, copy/paste [`examples/FIRST_RUN_PROMPT.md`](../examples/FIRST_RUN_PROMPT.md) into the AI environment where HiveForge is loaded. It guides the agent through a minimal safe intake, project inspection, workflow recommendation and first verified task.