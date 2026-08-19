# Security Analysis

## Document validation and upload attack

- Extension validation for `.txt`, `.md`, and `.pdf`
- MIME validation
- File size validation
- Empty file detection
- Duplicate file detection
- Safe filename restrictions
- Path traversal names and mismatched MIME/extension pairs are rejected before parsing
- Duplicate content hashes prevent repeated indexing

## Role-based access

The system supports three roles:

- student
- teacher
- admin

Role filtering is applied before retrieval so the model does not search privileged documents and then hide results later.

## RAG poisoning

Uploaded text is treated as evidence, not as executable instructions. Prompt-like strings in a document are still a residual poisoning risk because the current product is retrieval-only; a future LLM adapter must delimit and independently validate retrieved context.

## Data leakage and permission

Private documents carry owner and role metadata. Admins and owners can access them, while ordinary users are filtered before sources are returned. The current demo has no login provider, so the submitted user id is an application-level identity claim rather than cryptographic authentication.

## Prompt injection

Questions are checked by `PromptInjectionFilter` for instruction overrides, system-prompt extraction, code execution, template injection, role escalation, SQL patterns, and encoding tricks. Rejected questions never reach retrieval.

## Citation integrity

Citation strings are generated from the same metadata attached to the indexed chunk. Each result exposes citation number, filename, page, section, document id, and chunk id. This gives an auditable link from answer evidence to source metadata, but does not prove that a source is factually correct.

## Remaining risk

The in-memory index is not durable, the demo identity is not authenticated, PDF files may contain active or malformed content for downstream tooling, and there is no OCR or malware scanning. Production deployment needs authentication, storage isolation, audit logs, rate limits, and a sandboxed parser.

## Risk handling

- Unsafe filenames are rejected
- Duplicate content is blocked
- Documents are assigned role permissions before indexing
- Retrieval uses the role-aware metadata to enforce access control
