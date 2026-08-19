# Project Reflection

The difficult part of this project was not writing a cosine-similarity search. It was making the result inspectable as a product. The seven Engineering experiments were useful for learning, but asking a customer to assemble them would hide ownership boundaries and make upload, citation, and permission behavior impossible to accept formally. The Product now has its own source boundary, dataset, UI, tests, and reports.

One implementation issue exposed by testing was a citation-support control-flow gap: the answer was validated before its source metadata had been attached, so a valid retrieval could be downgraded to an unsupported response. Moving support evidence into the validation path made the UI result and the report agree. A second lesson was that “supports PDF” is not enough: page metadata must survive parsing and chunking so a reviewer can locate the evidence.

The remaining trade-off is deliberate: this release is retrieval-only because no external LLM backend is configured. That makes the citation behavior deterministic and honest, while leaving a clear next step for an LLM adapter, labelled accuracy evaluation, persistence, authentication, and OCR.
