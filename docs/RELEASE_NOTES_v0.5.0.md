# UNPS HiveForge v0.5.0

HiveForge v0.5.0 productionizes the portable agent-control package without turning optional integrations into mandatory runtime dependencies.

## Highlights

- synchronized package/BRAIN release metadata;
- production CI gate and secret/public-private scans;
- fresh-install coverage for Linux and macOS plus WSL validation gate;
- dashboard health smoke testing;
- live Graphify fixture extraction plus Graphify-absent fallback testing;
- package export/import round trip;
- dependency maturity registry;
- staged Composio and LangGraph profiles;
- ToolJet Agent & Capability Registry contract;
- yt-dlp preferred media-ingestion policy;
- immutable release artifact with SHA-256 checksum.

## Core versus optional capabilities

The HiveForge core package can be Production while optional capabilities retain independent maturity:

- Graphify — Candidate;
- yt-dlp — Candidate;
- Composio — Staged;
- LangGraph — Staged;
- ToolJet registry runtime — Staged.

Their absence must not break core HiveForge operation.

## Installation

After release publication:

```bash
HIVEFORGE_REF=v0.5.0 \
  curl -fsSL https://raw.githubusercontent.com/Bigper4mer/UnparalleledSource/v0.5.0/install.sh | sh

hiveforge doctor
hiveforge bootstrap
```

For downloaded release archives, verify `SHA256SUMS` before use.
