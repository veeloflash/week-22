# Model Analysis

## Retrieval method

The system uses SentenceTransformer Embedding, not TF-IDF.

## Generation mode

This environment does not provide a live external LLM backend, so the system is documented as a Retrieval-only prototype.

## Model details

- Model: sentence-transformers/all-MiniLM-L6-v2
- Embedding dimension: 384
- Retrieval method: SentenceTransformer Embedding
- Normalized cosine similarity is used for ranking

## Why this choice

- Real semantic retrieval is supported
- The product reflects actual embedding-based indexing and retrieval
- Output is consistent with the implementation and avoids unsupported claims

## Measurement notes

The project includes retrieval timing logic and uses high-level latencies recorded via `time.perf_counter()` in the retrieval pipeline. The 20-question Product set covers five subjects and is recorded in `product_evaluation.md`; it is a retrieval acceptance test, not a claim of generated-answer factual accuracy.

## Chunk and top-k tuning

The Product uses 350-character chunks with 50-character overlap. This keeps subject explanations together while allowing boundary terms to appear in adjacent chunks. The default top-k is 5: it gives enough evidence for source comparison without flooding the retrieval-only answer. A future evaluation should compare k=3, 5, and 8 using labelled relevance rather than choosing by latency alone.

## Accuracy and failure modes

The current evidence is pass/fail retrieval coverage for 20 representative questions. It does not provide a statistically meaningful accuracy score because there is no human-labelled relevance set and no external LLM answer generator. Known failures include ambiguous questions, unsupported topics, scanned PDFs, and semantically similar but incorrect chunks. The UI exposes scores and citations so these failures can be inspected.
