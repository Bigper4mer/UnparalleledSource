\# Graphify Codebase Intelligence Skill

Status: Candidate  
Version: 0.1.0  
Category: Coding / Architecture  
Depends on: \`GRAPHIFY\_CAPABILITY.md\`

\#\# Trigger  
Use this skill for non-trivial repository architecture, dependency, impact-analysis, onboarding, migration, or refactor tasks where understanding cross-file relationships before reading large portions of the repository will reduce context cost or improve correctness.

\#\# Objective  
Use Graphify as a progressive-disclosure layer between BRAIN and raw source code.

The graph narrows where to look. Source code, tests, build output, runtime evidence, and reviewed architecture decisions remain authoritative.

\#\# Decision Gate  
Before invoking Graphify, answer:  
1\. Is this a codebase/repository task?  
2\. Are the relevant files or relationships already known with high confidence?  
3\. Is the repository complex enough that relationship mapping will save repeated broad reads?  
4\. Is a recent \`graphify-out/graph.json\` already available?

If the task is small and bounded, skip Graphify.

If a graph exists and is reasonably fresh, query it before rebuilding.

If no graph exists, build one only when the expected reduction in search/context/rework justifies the cost.

\#\# Standard Sequence

\`\`\`text  
classify repository task  
  → inspect README / project state  
  → check graph freshness  
  → query existing graph OR build/update graph  
  → identify likely modules/files/nodes  
  → inspect exact source  
  → plan/implement  
  → targeted tests  
  → review \+ verify  
\`\`\`

\#\# Commands  
Initial graph:

\`\`\`bash  
graphify .  
\`\`\`

Architecture discovery:

\`\`\`bash  
graphify query "What are the major architectural boundaries and highest-connectivity components?"  
\`\`\`

Impact investigation:

\`\`\`bash  
graphify query "What components are affected by changing \<component\>?"  
\`\`\`

Relationship trace:

\`\`\`bash  
graphify path "\<node-a\>" "\<node-b\>"  
\`\`\`

Focused inspection:

\`\`\`bash  
graphify explain "\<node\>"  
\`\`\`

\#\# Context-Efficiency Contract  
Preferred hydration order:

\`\`\`text  
BRAIN / project instructions  
→ Graphify report or targeted query  
→ scoped subgraph / paths  
→ exact implicated source files  
→ tests/runtime evidence  
\`\`\`

Do not load \`graph.json\`, \`graph.html\`, the full repository, and all source files simultaneously unless a specific analysis requires it.

Use \`GRAPH\_REPORT.md\` for orientation; use targeted query/path/explain for navigation; use raw files for verification.

\#\# Evidence Rules  
Graph edges can be explicit or inferred.  
\- \`EXTRACTED\`: explicit relationship found in source; still validate when material.  
\- \`INFERRED\`: derived relationship; treat as a lead/hypothesis until verified.  
\- ambiguous relationships must not become architectural facts without corroboration.

For any consequential claim, preserve the source file/location and verify the relevant implementation directly.

\#\# Recommended UNPS Uses  
\#\#\# New-codebase bootstrap  
Generate a graph after the normal README/repo inspection when the codebase is large enough. Use communities and god nodes to create a compact architecture orientation before assigning tickets.

\#\#\# Refactor planning  
Use graph paths and affected relationships to identify seams, likely blast radius, shared dependencies, and test surfaces before creating the implementation plan.

\#\#\# Debugging  
Use Graphify only when the failure crosses modules or the call/dependency path is unclear. Do not replace ROOT\_CAUSE\_VERIFICATION or runtime debugging with static graph inference.

\#\#\# Multi-agent work  
The coordinator may use Graphify to produce narrow context packets for specialists. Workers receive only the implicated modules/files, relevant path/subgraph, requirements, and acceptance criteria.

\#\#\# Code review  
Use the graph to ask whether a change touched a high-connectivity/god node or crosses architectural boundaries, then inspect the actual diff/tests.

\#\# Freshness Rule  
A graph is potentially stale when source topology has materially changed since it was generated. Rebuild/update when:  
\- new modules/packages were added;  
\- significant imports/calls/inheritance changed;  
\- a broad refactor or dependency migration occurred;  
\- Graphify reports stale/failed output;  
\- the answer depends on relationships modified after the graph timestamp.

Do not rebuild merely because a few local implementation lines changed when topology is unaffected.

\#\# Mixed-Source Rule  
Graphify can map docs/media with optional semantic backends, but normal coding use should remain code-first and local. For client or regulated sources, do not enable semantic/API processing until the project's data-sharing rules permit it.

\#\# Completion Gate  
When Graphify materially influences an implementation decision, record:  
\- graph version/timestamp;  
\- query/path used;  
\- files subsequently verified;  
\- whether the graph conclusion matched source truth;  
\- any false/ambiguous edge worth capturing as a learning or regression test.

\#\# Fallback  
If Graphify is unavailable:  
1\. use repository-native search/navigation;  
2\. inspect manifests/imports/references;  
3\. use a targeted repo packaging/indexing tool if available;  
4\. proceed with exact source reads.

Never block a task solely because Graphify is missing.  
