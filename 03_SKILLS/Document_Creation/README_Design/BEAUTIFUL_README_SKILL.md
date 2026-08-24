\# UNPS Beautiful README Skill

Status: Candidate  
Version: 0.1.0  
Owner: Unparalleled Source

\#\# Purpose  
Create polished, visually strong, accurate README.md files for UNPS repositories, Custom Agent packages, skills, workflows, tools, and client-facing technical projects.

\#\# Source Patterns  
This skill is adapted from strong open-source README practices, especially easyReadme-style repository-grounded generation, Standard Readme structure, and curated beautiful-README pattern libraries. Use the ideas, not copied prose or ornamental clutter.

\#\# Trigger  
Use when creating, refreshing, or polishing a README.md; documenting a Custom Agent package; preparing a repository for handoff; or when a technical project needs a professional landing page.

\#\# Grounding Rule  
Inspect the actual repository or agent package before writing. Do not invent commands, features, routes, dependencies, screenshots, badges, licenses, deployment URLs, or support channels. Missing facts become TODOs or are omitted.

\#\# README Architecture  
Choose sections based on the project rather than forcing every section:  
1\. Hero: logo/mark when available, project name, one-line value proposition.  
2\. Status row: only verifiable badges or concise metadata.  
3\. Visual proof: screenshot, GIF, architecture image, or product preview when it materially helps.  
4\. Why it exists / Overview.  
5\. Key capabilities or features.  
6\. Quick start.  
7\. Installation and prerequisites.  
8\. Usage with verified examples.  
9\. Architecture / How it works when useful.  
10\. Configuration and environment variables without exposing secrets.  
11\. Workflows, skills, models, MCPs, or dependencies when the repository is agentic.  
12\. Testing / validation.  
13\. Deployment when applicable.  
14\. Roadmap or known limitations when useful.  
15\. Contributing / support / license when applicable.

\#\# Visual Rules  
\- Use a strong hierarchy and short sections.  
\- Prefer one useful hero visual over many decorative assets.  
\- Badges must communicate real status; avoid badge walls.  
\- Use GitHub-flavored Markdown tables only for information that scans better as a matrix.  
\- Use callouts, details/summary, code blocks, Mermaid diagrams, and aligned image rows sparingly.  
\- Keep the README attractive in both light and dark GitHub themes.  
\- Use descriptive image alt text.  
\- Avoid excessive emojis, animated clutter, vanity counters, and unsupported claims.

\#\# Agent Package README  
For Custom Agent builds, include: purpose, abilities, BRAIN.md role, included skills/workflows, preferred models/harnesses, MCP/dependency requirements, install/deploy steps, example tasks, context-budget notes, verification behavior, and version/status.

\#\# Documentation Accuracy Gate  
Before completion verify:  
\- Local links and referenced files exist.  
\- Commands match package scripts or documented tool usage.  
\- Routes/endpoints match the project.  
\- Environment variables are real and secrets are never embedded.  
\- Badges point to the correct repository/service.  
\- Screenshots reflect the current product when provided.  
\- Installation steps are executable or clearly labeled unverified.

\#\# Style  
Professional, modern, scan-friendly, concise, and useful. The README is the landing page for the project; it should explain value before implementation detail.

\#\# Token Rule  
Inspect selectively. Start with repository tree, package/manifest files, existing README, key entry points, config, and deployment files. Load deeper files only when needed to verify a claim.  
