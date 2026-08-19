# Testing Report

## Scope

The test suite exercises the Product-critical behaviors: PDF/TXT/Markdown ingestion, chunk segmentation, retrieval method declaration, permission filtering, prompt filtering, citation format, and the 20-question acceptance set. The seven Engineering experiments are deliberately excluded from this report.

## Verification

The current regression suite is executed with pytest and checks the product requirements before release.

## Example evidence

- Chunk size changes segmentation lengths
- Retrieval method is explicitly embedding-based
- Permission filtering restricts private documents to admin access
- Citation output includes citation number, Source, Page, Section, and Chunk metadata

## Coverage notes

The shipped Product dataset contains 56 files. The detailed acceptance evidence is in `product_evaluation.md`; security and failure cases are covered by `test_prompt_injection.py`, `test_permissions.py`, and `test_upload_security.py`.
