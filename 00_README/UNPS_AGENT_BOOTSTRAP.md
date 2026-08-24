\# UNPS Agent Bootstrap

Version: 0.1.0  
Status: Candidate  
Owner: Unparalleled Source  
Updated: 2026-08-23

\#\# Purpose  
Use this file at the beginning of a fresh agent or coding session to hydrate only the minimum required UNPS capabilities.

\#\# Startup Procedure  
1\. Inspect the current project/repository/workspace before making changes.  
2\. Identify the task domain: research, government capture, procurement, document production, coding, SEO, cinematography, or another defined category.  
3\. Read \`00\_README/LIBRARY\_INDEX.md\`.  
4\. Resolve the narrowest applicable Custom Agent build or System Instruction.  
5\. Load the workflow required for the task.  
6\. Load only the referenced skills.  
7\. Resolve preferred MCPs/connectors and dependencies.  
8\. Confirm output schema and evaluation criteria.  
9\. Execute with minimal context duplication.  
10\. After completion, capture proven reusable improvements back into the library as Candidate assets.

\#\# Default Operating Rules  
\- Prefer existing UNPS assets over recreating equivalent instructions.  
\- Do not load every skill into every session.  
\- Do not add dependencies without a demonstrated need.  
\- Prefer the simplest implementation that solves the current problem.  
\- Reuse standard libraries and existing project patterns before adding packages.  
\- Fix root causes rather than layering patches.  
\- Preserve validation, security, accessibility, and data-integrity safeguards.  
\- For current-information research, favor recent-source workflows and then verify important claims with primary or authoritative sources.  
\- For connected Workspace tasks, use the relevant Google Workspace connector instead of asking for manual exports when the connector can resolve the data.  
\- Separate verified source facts from inference and recommendations.  
\- Never treat a reference PDF as the sole canonical source when an editable prompt/skill can be maintained.

\#\# Context Budget Rule  
Every loaded asset must justify its context cost. If a capability is not required for the current task, reference it in the manifest but do not inject its full contents.

\#\# Hardening Loop  
Real workflow \-\> extract reusable pattern \-\> create Candidate asset \-\> test on another real task \-\> evaluate \-\> revise \-\> promote to Production.

\#\# Custom Agent Packaging  
A deployable agent should eventually contain or reference:  
\- AGENT.md  
\- SYSTEM\_INSTRUCTIONS.md  
\- SKILLS.md  
\- WORKFLOWS.md  
\- MCP\_PREFERENCES.md  
\- DEPENDENCIES.md  
\- TOOL\_POLICY.md  
\- OUTPUT\_SCHEMAS.md  
\- INSTALL.md  
\- CHANGELOG.md

\#\# Maturity States  
Experimental \-\> Candidate \-\> Production \-\> Deprecated.

Do not skip testing when moving Candidate assets to Production.  
