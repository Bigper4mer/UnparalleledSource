\# UNPS MCP / Connector / Capability Registry

Version: 0.2.0  
Status: Candidate  
Owner: Unparalleled Source  
Updated: 2026-08-24

\#\# Purpose  
Maintain preferred tool, connector, CLI, and capability routing for UNPS agents. This registry is not a mandate to call every tool. Agents should use the smallest set that materially improves the task.

\#\# Preferred Routing

\#\#\# Google Workspace  
Use for connected UNPS operational data and write actions when available.  
\- Google Drive: project files, prompt library, source documents, workspace hydration  
\- Gmail: correspondence research, outreach, replies, drafts, inbox/outbox evidence  
\- Google Calendar: deadlines, accountability events, meeting coordination  
\- Google Contacts: recipient and attendee resolution

\#\#\# GitHub  
Use for repository inspection, coding workflows, source-controlled skills, reusable engineering patterns, open-source comparison, and technical due diligence.

\#\#\# Only-CLI \`oc\`  
Use as a token-efficient, text-first public-web retrieval capability when a known page must be read and full browser rendering is unnecessary.

Preferred install:

\`\`\`bash  
npm install \-g @only-cli/oc  
\`\`\`

One-off fallback:

\`\`\`bash  
npx @only-cli/oc open \<url\>  
\`\`\`

Requirements: Node.js 20+.

Route to \`oc\` when the page is public, text is the primary evidence, and minimizing markup/context overhead matters. Escalate to Firecrawl, browser automation, or visual inspection when structured crawling, JavaScript interaction, authenticated state, forms, or visual layout are required.

Canonical capability file: \`06\_DEPENDENCIES/Node/CLI\_Tools/ONLY\_CLI\_OC\_CAPABILITY.md\`.

\#\#\# Firecrawl  
Use for structured live-web extraction, site/document scraping, crawling, and research tasks where repeatable page-level extraction improves reliability.

\#\#\# Web / Current Research  
Use for current public information, source discovery, citations, and broad research. For recent-intelligence tasks, favor a recent-source workflow and verify material claims with primary or authoritative sources.

\#\#\# Browser Automation  
Use when JavaScript interaction, forms, multi-step navigation, authenticated state, or browser behavior is materially required. Do not launch a full browser when a cheaper text-first retrieval path is sufficient.

\#\#\# Domain-Specific Connectors / APIs  
Use specialized connectors or APIs when they have unique first-party or structured data that materially outperforms generic web search. Avoid stacking overlapping tools without a reason.

\#\# Retrieval Cost Ladder  
For web/content retrieval, prefer the least expensive reliable path:  
1\. First-party connected source or local/project file.  
2\. Deterministic/local text extraction when the source is already available.  
3\. Only-CLI \`oc\` for a known public text-centric page.  
4\. Web/search for discovery, freshness, and citations.  
5\. Firecrawl for structured extraction/crawling.  
6\. Browser automation for interactive/JS-dependent work.  
7\. Visual browser/screenshot inspection when layout is decision-critical.

Escalate only when the lower-cost path cannot reliably answer the task.

\#\# Tool Selection Rules  
1\. Prefer first-party connected data for questions about UNPS-owned files, email, calendar, repositories, or records.  
2\. Prefer primary public sources for laws, solicitations, official pricing, filings, and authoritative technical documentation.  
3\. Use the lightest retrieval method that preserves required evidence quality.  
4\. Use web search for discovery/recency and extraction tools for source capture or structured parsing.  
5\. Use GitHub when the task concerns a repository, code, agent skill, engineering pattern, or open-source alternative.  
6\. Do not call multiple overlapping tools merely because they are available.  
7\. Keep credentials, secrets, and sensitive tokens outside portable agent files.  
8\. Store setup requirements and environment variables in dependency manifests using placeholder names only.  
9\. New external capabilities begin as Pilot/Candidate until tested on real UNPS work.

\#\# Capability Profile Pattern  
Each production Custom Agent may reference a profile containing:  
\- required connectors/tools  
\- preferred connectors/tools  
\- optional capabilities  
\- fallback/escalation order  
\- read/write permissions  
\- trigger conditions  
\- prohibited or unnecessary tools  
\- installation/runtime requirements  
\- authentication notes without secrets  
\- maturity state and verification date

\#\# Initial Profiles to Build / Harden  
\- Government Capture  
\- Procurement Intelligence  
\- Research Intelligence  
\- Document Production  
\- Software Development / Codex  
\- SEO Intelligence  
\- Cinematography / Media Generation

\#\# Maintenance Rule  
When a real workflow shows that a different connector, CLI, API, or routing order is consistently better, update the profile and run regression tests before promoting the change. Remove or demote capabilities that create more maintenance, risk, or context cost than value.  
