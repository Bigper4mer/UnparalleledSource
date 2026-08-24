\# Graphify Codebase Intelligence Capability

Status: Candidate  
Version: 0.1.0  
Validated upstream: Graphify-Labs/graphify 0.9.48  
Package: \`graphifyy\`  
CLI: \`graphify\`  
Owner: Unparalleled Source

\#\# Purpose  
Use Graphify as an optional repository-intelligence accelerator for non-trivial codebase work. It converts source structure into a queryable knowledge graph so agents can inspect architecture, dependencies, communities, call relationships, rationale links, and impact paths before broadly hydrating raw source files.

Graphify is an index and reasoning aid, not an authoritative substitute for source code, tests, runtime behavior, or human-reviewed architecture decisions.

\#\# Why It Fits UNPS  
Graphify supports the UNPS context-efficiency model: inspect relationships first, then load only the exact source files needed to verify or implement a change. Code parsing is local and deterministic through tree-sitter; Graphify distinguishes explicit/extracted relationships from inferred relationships.

\#\# Validated Upstream State  
The current validated release for this capability is \`0.9.48\`, published from commit \`b2cd36267456c166788c95be6e68574064a92a42\` on 2026-08-20.

Minimum Python: 3.10+.

Core dependencies include NetworkX, NumPy, RapidFuzz, tree-sitter, and language grammar packages. Optional extras exist for MCP, PDFs, Office documents, Google data, video/audio, graph databases, and model backends. Do not install optional extras unless the workflow needs them.

\#\# Installation  
Preferred isolated installation:

\`\`\`bash  
uv tool install graphifyy==0.9.48  
graphify install \--project \--platform codex  
\`\`\`

Generic Agent Skills registration when appropriate:

\`\`\`bash  
graphify install \--platform agents  
\`\`\`

Alternative isolated installation:

\`\`\`bash  
pipx install graphifyy==0.9.48  
\`\`\`

Avoid unpinned production installation until the dependency audit validates a newer release.

\#\# Core Workflow  
Build or refresh a graph only when repository complexity justifies the work:

\`\`\`bash  
graphify .  
\`\`\`

Expected output contract:

\`\`\`text  
graphify-out/  
├── graph.html  
├── GRAPH\_REPORT.md  
└── graph.json  
\`\`\`

Then prefer graph queries before broad source reads:

\`\`\`bash  
graphify query "What are the major architectural boundaries?"  
graphify path "\<node-a\>" "\<node-b\>"  
graphify explain "\<node\>"  
\`\`\`

\#\# Trigger Conditions  
Use Graphify when one or more are true:  
\- repository spans multiple modules/packages and a change crosses boundaries;  
\- architecture or dependency relationships are unclear;  
\- planning a large refactor or migration;  
\- investigating blast radius / affected components;  
\- onboarding to an unfamiliar codebase;  
\- repeated grep/search operations are consuming large context;  
\- identifying god nodes, subsystem communities, cross-file calls/imports/inheritance, or rationale/ADR links materially improves the decision.

Do not require Graphify for:  
\- trivial single-file edits;  
\- narrowly scoped bugs where the relevant files are already known;  
\- small repositories whose structure is obvious;  
\- tasks where running/building the graph costs more than targeted source inspection.

\#\# Routing Pattern

\`\`\`text  
BRAIN  
  → repository-complexity gate  
  → fresh Graphify graph available?  
      yes → query/path/explain  
      no  → build only if expected value \> cost  
  → retrieve exact implicated files  
  → verify against source/tests/runtime  
  → implement/review/verify  
\`\`\`

\#\# Data & Security Posture  
\- Code analysis is local-first and does not require an LLM for structural extraction.  
\- Semantic processing of documents/media can invoke configured model/API backends. Treat this as external data transfer and apply project/client sensitivity rules before enabling it.  
\- Never include credentials, \`.env\` secrets, private keys, regulated data, or unnecessary client material in graph inputs.  
\- Treat \`INFERRED\` edges as hypotheses until corroborated where they influence consequential work.  
\- Preserve source locations and provenance when using graph evidence.

\#\# Optional Extras Policy  
Install only on demand, after dependency/security review:  
\- MCP: only when Graphify needs to be exposed through MCP rather than CLI/skill routing.  
\- PDF/Office/Google: only for mixed-repository knowledge mapping.  
\- Video/audio: only for approved media-ingestion workflows; note that the upstream video extra uses yt-dlp.  
\- Neo4j/FalkorDB/Postgres: only when an external graph persistence layer is explicitly required.

The normal UNPS codebase use case requires only the core package.

\#\# Test Status  
\#\#\# Contract smoke test — PASS  
A local UNPS smoke test validated the expected Graphify-style NetworkX node-link contract and downstream path/explain behavior using the runtime's installed NetworkX.

Observed environment:  
\- Python 3.13.5  
\- uv 0.10.0  
\- NetworkX 3.6.1

Assertions passed:  
\- node-link graph parses;  
\- nodes and edges preserve relationship structure;  
\- shortest path resolution works;  
\- node explanation/neighbor inspection works;  
\- downstream code can consume the expected \`graph.json\` shape.

\#\#\# Live package/extraction test — BLOCKED BY SANDBOX NETWORK  
\`uv tool install graphifyy\` was attempted in the current sandbox. Installation could not reach PyPI because outbound DNS resolution for \`pypi.org\` is unavailable in this runtime. This is an environment limitation, not evidence of an upstream Graphify failure.

Therefore this capability remains \*\*Candidate\*\*, not Production.

\#\# Production Promotion Gate  
Before promotion, run in a networked coding harness:

\`\`\`bash  
uv tool install graphifyy==0.9.48  
graphify \--version  
graphify install \--project \--platform codex  
graphify .  
test \-f graphify-out/graph.json  
test \-f graphify-out/GRAPH\_REPORT.md  
test \-f graphify-out/graph.html  
graphify query "What are the major architectural boundaries?"  
\`\`\`

Then verify at least one \`path\` result and one \`explain\` result against the actual source files. Record runtime, duration, repository size, graph size, and whether Graphify reduced source/context reads during a real UNPS coding task.

\#\# Maintenance  
Re-check upstream version and dependency/security posture before changing the pinned validation version. Update this capability only after a new release passes the same integration gate.  
