\# UNPS Source Ingestion Normalization

Status: Candidate  
Version: 0.1.0  
Owner: Unparalleled Source

\#\# Purpose  
Reduce token and context waste by normalizing source files into agent-friendly text before repeated analysis while preserving the authoritative original.

\#\# Default Rule  
Markdown is the preferred canonical ingestion format for text-heavy source material. Plain text is the fallback. PDF is an evidence/presentation format and should not be repeatedly loaded in full when a faithful Markdown/text representation is available.

\#\# PDF → Markdown Rule  
When a PDF is introduced and the task will require repeated reference:  
1\. Preserve the original PDF unchanged as the authoritative visual/source artifact.  
2\. Extract or convert its readable text once into Markdown or plain text.  
3\. Preserve heading hierarchy, page references when materially useful, tables where conversion is reliable, source URLs, dates, and identifiers.  
4\. Store the normalized file beside or beneath the source using an obvious relationship such as \`SOURCE\_NAME.ingested.md\`.  
5\. Use the normalized Markdown for routine retrieval, searching, summarization, quoting, planning, and agent handoffs.  
6\. Re-open the original PDF only for visual/layout questions, figures, diagrams, signatures, scanned pages, complex tables, footnotes, or when conversion fidelity is uncertain.

\#\# Markdown-First Rule  
If both PDF and Markdown versions exist, use Markdown first for semantic reasoning. Do not ingest both copies into the same context unless cross-checking fidelity.

\#\# Chunking Rule  
Do not load an entire long normalized source by default. Retrieve only the sections required for the current task. Prefer heading-aware chunks and preserve enough surrounding context to avoid changing meaning.

\#\# Source Manifest  
For important project sources maintain lightweight metadata:  
\- original file name and format  
\- normalized file name  
\- source authority/type  
\- source date / as-of date  
\- conversion date  
\- conversion method when material  
\- fidelity notes / known extraction gaps  
\- canonical original link or file ID

\#\# Visual Exception  
PDFs, slides, images, and spreadsheets may contain meaning not captured by text extraction. Use multimodal/original-file inspection when the task concerns charts, page layout, form fields, spatial relationships, screenshots, handwriting, signatures, or other visual evidence.

\#\# OCR Rule  
OCR is a last resort for scanned sources when direct text extraction or native visual reading cannot recover the required information. Do not batch OCR a document merely for convenience.

\#\# Duplicate Control  
Do not create multiple normalized copies for the same unchanged source. Update or version the canonical normalized copy when the original materially changes.

\#\# Retrieval Budget  
Use this sequence:  
1\. source manifest / index  
2\. normalized Markdown headings  
3\. relevant chunks  
4\. original file pages only as needed  
5\. external research only if the task requires information beyond the source

\#\# Accuracy Gate  
Normalization must never silently alter numbers, dates, named entities, legal language, solicitation requirements, table relationships, or source attribution. When fidelity is uncertain, flag the uncertainty and consult the original.

\#\# Output Rule  
Generated PDFs remain publication artifacts. Whenever practical, retain an editable Markdown, Google Doc, DOCX, or structured source so future agents do not have to reverse-ingest the published PDF.  
