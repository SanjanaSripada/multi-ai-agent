# Smart Multi-Agent AI Processor
Flask multi-agent system with AI that handles Email, JSON, and PDF inputs smartly through some agents and saves each of the entries in an SQLite database.

## Features
- Inputs can be received in Email, JSON, or PDF.
- Infers the input type automatically and invokes the corresponding agent:
**Email Agent** – Extracts sender, subject, and urgency.
**JSON Agent** – Parses structured data and extracts useful fields.
**PDF Agent** – Pulls text out of resumes/documents and summarizes them.
- Classifies intent from the input (e.g., RFQ, Invoice, Complaint, Regulation).
- Stores data logged into a SQLite database by a Memory Manager.
- Clean and responsive Web UI with Bootstrap styling.
  
