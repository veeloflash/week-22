# Implementation 6 Testing Report

- Compared different chunk sizes, Top-K values, and embedding models.
- Generated a performance table and a chart summarizing retrieval quality.

## Performance Table
- Chunk size 100, Top-K 1, TF-IDF: top docs [1], avg score 0.541
- Chunk size 100, Top-K 1, MiniLM: top docs [1], avg score 0.541
- Chunk size 100, Top-K 3, TF-IDF: top docs [1, 4, 2], avg score 0.247
- Chunk size 100, Top-K 3, MiniLM: top docs [1, 4, 2], avg score 0.247
- Chunk size 100, Top-K 5, TF-IDF: top docs [1, 4, 2, 3, 5], avg score 0.148
- Chunk size 100, Top-K 5, MiniLM: top docs [1, 4, 2, 3, 5], avg score 0.148
- Chunk size 300, Top-K 1, TF-IDF: top docs [1], avg score 0.541
- Chunk size 300, Top-K 1, MiniLM: top docs [1], avg score 0.541
- Chunk size 300, Top-K 3, TF-IDF: top docs [1, 4, 2], avg score 0.247
- Chunk size 300, Top-K 3, MiniLM: top docs [1, 4, 2], avg score 0.247
- Chunk size 300, Top-K 5, TF-IDF: top docs [1, 4, 2, 3, 5], avg score 0.148
- Chunk size 300, Top-K 5, MiniLM: top docs [1, 4, 2, 3, 5], avg score 0.148
- Chunk size 500, Top-K 1, TF-IDF: top docs [1], avg score 0.541
- Chunk size 500, Top-K 1, MiniLM: top docs [1], avg score 0.541
- Chunk size 500, Top-K 3, TF-IDF: top docs [1, 4, 2], avg score 0.247
- Chunk size 500, Top-K 3, MiniLM: top docs [1, 4, 2], avg score 0.247
- Chunk size 500, Top-K 5, TF-IDF: top docs [1, 4, 2, 3, 5], avg score 0.148
- Chunk size 500, Top-K 5, MiniLM: top docs [1, 4, 2, 3, 5], avg score 0.148
