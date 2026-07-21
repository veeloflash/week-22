# Implementation 7 Testing Report

- Analyzed three major failure modes: retrieval failure, context failure, and knowledge failure.
- Proposed practical improvements for each failure category.

## Failure Analysis
- Retrieval Failure: The top-ranked chunk does not contain the answer.
  Impact: Low recall on relevant passages.
  Fix: Increase Top-K and improve embedding quality.
- Context Failure: The retrieved context is too short or too noisy.
  Impact: The model misses the supporting evidence.
  Fix: Use larger chunk windows and better reranking.
- Knowledge Failure: The knowledge base lacks the needed fact.
  Impact: The system answers incorrectly despite good retrieval.
  Fix: Expand the corpus and add curated domain knowledge.
