Python: 3.10  
sentence-transformers: 2.6.0  
Model: all-MiniLM-L6-v2  
OS: Windows 11  

# Chunk
Total chunks: 5  
Each chunk contains:

- id
- text
- source
- page

# Query
Query 1: How does RAG reduce hallucination?
Query 2: What is semantic search?
Query 3: How do embeddings work?

# Process
1. Load MiniVectorDB
2. Add chunks into database
3. Change chunk texts into vectors
4. Change query into vector
5. Compute Cosine similarity
6. Compute Euclidean distance
7. Return Top-K results

# Test result
## How does RAG reduce hallucination?
Cosine Top‑K:
