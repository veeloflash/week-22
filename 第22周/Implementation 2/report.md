# Implementation 2 Testing Report

- Built a vector index with FAISS when available, otherwise used a NumPy fallback.
- Compared Top-K values 1, 3, and 5.

## Result Summary
### Top-1
- Doc 2 score=0.996
### Top-3
- Doc 2 score=0.996
- Doc 1 score=0.993
- Doc 5 score=0.862
### Top-5
- Doc 2 score=0.996
- Doc 1 score=0.993
- Doc 5 score=0.862
- Doc 4 score=0.584
- Doc 3 score=0.458
