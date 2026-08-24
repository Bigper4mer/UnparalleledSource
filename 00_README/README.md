\# Unparalleled Source Prompt & Agent Library

Version: 0.1.0  
Status: Foundation build  
Canonical workspace: PROMPTS.UNPS

\#\# Purpose

This Drive is the canonical Unparalleled Source library for reusable prompts, system instructions, skills, workflows, MCP/connector preferences, dependencies, output schemas, evaluations, and portable Custom Agent builds.

\#\# Operating model

Real UNPS work \-\> identify repeated behavior \-\> extract reusable workflow \-\> separate prompt / skill / tool policy \-\> test against another real job \-\> refine \-\> promote to production \-\> include in applicable Custom Agent builds.

\#\# Core architecture

\- 00\_README — library governance, index, naming, changelog  
\- 01\_SYSTEM\_INSTRUCTIONS — reusable system-level instructions  
\- 02\_PROMPTS — task prompts organized by domain  
\- 03\_SKILLS — reusable capability packages  
\- 04\_MCP\_CONNECTORS — preferred MCPs/connectors and usage policies  
\- 05\_WORKFLOWS — repeatable multi-step operating procedures  
\- 06\_DEPENDENCIES — dependency manifests and runtime requirements  
\- 07\_TEMPLATES — standard templates for prompts, skills, agents and workflows  
\- 08\_OUTPUT\_SCHEMAS — repeatable output structures  
\- 09\_TESTS\_EVALS — regression tests, examples and quality rubrics  
\- 10\_CUSTOM\_AGENTS — portable deployable agent builds  
\- 99\_ARCHIVE — deprecated and superseded assets

\#\# Source-of-truth rule

Markdown/plain text is preferred for portable agent assets. Google Docs may be maintained as human-editable companions. PDFs are reference/published artifacts and should not be the only canonical copy of a prompt or skill.

\#\# Version states

experimental \-\> candidate \-\> production \-\> deprecated

\#\# Context-efficiency rule

Do not load the entire library into an agent. Resolve the current task, then load only the applicable system instruction, workflow, skills, MCP/tool policy, dependencies and output schema.

\#\# Current migrated assets

\- SWOT / market research prompt \-\> 02\_PROMPTS/Research\_SWOT  
\- Codex SEO agents prompt pack \-\> 02\_PROMPTS/SEO  
\- Video analyzer / cinematography prompt \-\> 02\_PROMPTS/Video\_Cinematography

\#\# Custom Agent packaging standard

Each deployable agent should contain at minimum:

AGENT.md  
SYSTEM\_INSTRUCTIONS.md  
SKILLS.md or skill references  
WORKFLOWS.md  
MCP\_PREFERENCES.md  
DEPENDENCIES.md  
TOOL\_POLICY.md when needed  
OUTPUT\_SCHEMAS.md or schema references  
INSTALL.md  
CHANGELOG.md

\#\# Governance

Prefer reuse over duplication. Do not silently overwrite production assets. Preserve previous versions through version history or archive when materially superseded. Record meaningful changes in the changelog. Promote patterns based on proven UNPS workflows rather than speculative prompt accumulation.  
