\# UNPS Model & Harness Router

Status: Candidate  
Version: 0.1.0  
Owner: Unparalleled Source

\#\# Purpose  
Map abstract capability roles from BRAIN.md to the best available model, harness, and tool configuration without coupling workflows to one vendor.

\#\# Selection Principles  
Choose based on capability fit first, then risk, context size, latency, cost, modality, repo access, connector access, and verification requirements. Prefer the smallest capable configuration.

\#\# Capability Roles

\#\#\# Coordinator  
Best for decomposition, dependency tracking, integration, and final synthesis.  
Required: strong instruction following, long-context management, tool orchestration, and reliable structured output.

\#\#\# Deep Reasoner  
Best for ambiguous architecture, difficult debugging, strategic analysis, and high-risk synthesis.  
Required: strong reasoning, cross-source reconciliation, uncertainty handling.

\#\#\# Fast Worker  
Best for bounded edits, extraction, transformations, repetitive cleanup, and low-risk subtasks.  
Required: low latency and good instruction adherence.

\#\#\# Code Specialist  
Best for repository work, implementation, tests, refactors, code review, and shell/tool use.  
Preferred harnesses: Codex, Claude Code, Cursor, GitHub Copilot, or equivalent repo-aware coding agents.

\#\#\# Visual Specialist  
Best for UI/UX, screenshots, diagrams, decks, PDFs, and layout QA.  
Required: multimodal vision and artifact awareness.

\#\#\# Research Specialist  
Best for current intelligence, source discovery, primary-source verification, and evidence tables.  
Required: web/search connectors, citation discipline, source-date awareness.

\#\# Harness Routing  
\- Codex: preferred for repository-first engineering, command execution, implementation, tests, and agentic coding workflows.  
\- Claude Code: strong alternative for skill-driven coding, long-context repo analysis, and multi-step engineering workflows.  
\- Cursor: preferred when interactive IDE edits and human-in-the-loop review matter.  
\- GitHub Copilot: useful for GitHub-native workflows and spec-kit integrations.  
\- Browser/Research harness: preferred for current-source discovery and public-web verification.  
\- Workflow runners such as n8n: preferred for deterministic recurring integrations and event-driven automation.  
\- Local model harnesses: eligible when privacy, offline operation, or cost control outweighs frontier-model quality.

\#\# Multi-Model Execution Pattern  
1\. Coordinator defines work packages and acceptance criteria.  
2\. Assign each package to the cheapest/fastest model that can reliably complete it.  
3\. Escalate uncertain or high-risk tasks to a deeper model.  
4\. Use separate models for independent review when material risk exists.  
5\. Reconcile outputs through the coordinator.  
6\. Verify with tools/tests/sources rather than majority vote.

\#\# Cross-Model Review  
For high-impact outputs, prefer diversity: implementation model \!= review model when feasible. Use a second model to challenge assumptions, inspect diffs, or audit evidence. Disagreement triggers evidence gathering, not arbitrary voting.

\#\# Context Isolation  
Specialists receive only the minimum relevant files, requirements, constraints, and expected output. Do not forward the entire conversation by default. Return compact findings and artifact references to the coordinator.

\#\# Cost Control  
Use a routing ladder:  
1\. deterministic tool or script when sufficient;  
2\. fast/cheap model for bounded work;  
3\. specialist model for domain-heavy work;  
4\. deep reasoning model only for complexity or risk that justifies it.

\#\# Model Registry  
Maintain model-specific mappings as replaceable entries with: provider, model, supported modalities, context, tool support, ideal roles, known weaknesses, relative cost, latency, and last validation date.

\#\# Harness Registry  
Maintain harness entries with: repo access, shell access, browser access, MCP support, subagents, parallelism, approval model, file editing, testing/deployment capability, and supported model providers.

\#\# Fallback  
If a named model/harness is unavailable, use the closest role-equivalent option. Workflows must remain portable.

\#\# Validation  
Before promoting a model/harness mapping, test it against representative UNPS workloads and record quality, speed, cost, and failure modes in 09\_TESTS\_EVALS.  
