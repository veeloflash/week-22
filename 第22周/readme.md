# Week22 Engineering

This folder contains experimental implementations and analysis for Week 22 of the AI engineering assignment. Each subfolder demonstrates a different retrieval, vector database, or RAG-related concept.

## Project Structure

- `Implementation1/` - Mini vector database and chunking report
  - `Vector_Database.py` implements a basic embedding-based vector search engine using `sentence-transformers`.
  - `program report.md` describes chunk creation, query examples, and the role of RAG in reducing hallucination.
- `Implementation2/` - FAISS search demo
  - `faiss_search.py` builds a FAISS L2 index and performs nearest-neighbor search on sentence embeddings.
- `Implementation3/` - Chunking utility
  - `chunk.py` shows how to split text into fixed-size chunks for downstream retrieval or indexing.
- `Implementation4/` - Semantic retrieval example
  - `retrieval.py` implements a simple semantic retrieval engine using sentence embeddings and vector similarity.
- `Implementation5/` - Mini RAG prototype
  - `rag.py` demonstrates a retrieval-augmented generation flow with a fake LLM and permission filtering.
- `Implementation6/` - Performance evaluation
  - `performance.py` evaluates chunk sizing and retrieval accuracy.
- `Implementation7/` - Failure analysis
  - `failure_analysis.py` contains simple failure-mode checks for retrieval results.

## Dependencies

- Python 3.10
- `numpy`
- `sentence-transformers`
- `faiss` (for `Implementation2`)

## Usage

1. Install dependencies in a Python environment.
   ```powershell
   python -m pip install numpy sentence-transformers faiss-cpu
   ```
2. Run individual implementation scripts to explore each concept.
   ```powershell
   python .\Implementation1\Vector_Database.py
   python .\Implementation2\faiss_search.py
   python .\Implementation3\chunk.py
   python .\Implementation4\retrieval.py
   python .\Implementation5\rag.py
   python .\Implementation6\performance.py
   python .\Implementation7\failure_analysis.py
   ```

## Notes

- `Implementation1` and `Implementation5` focus on the end-to-end retrieval and RAG workflow.
- `Implementation2` shows how to leverage FAISS for efficient vector search.
- `Implementation3` and `Implementation6` are useful for understanding how chunk size impacts retrieval and performance.
- `Implementation7` highlights common retrieval failure scenarios.

## Related Project

A companion AI knowledge base assistant project exists in `Week22_AI_Knowledge_Base_Assistant/`, which includes a small Flask app, upload manager, and mini RAG system.
