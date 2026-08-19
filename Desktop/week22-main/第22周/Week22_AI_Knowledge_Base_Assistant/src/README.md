# Product Source Package

This is the public source boundary for the AI Knowledge Base Assistant. It exposes the product services used by the Flask application:

- `vector_database.py`: embedding storage and cosine search
- `retrieval.py`: top-k retrieval and role filtering
- `rag.py`: grounded answer and citation orchestration
- `upload.py`: PDF/TXT/Markdown validation, parsing, chunking, and indexing
- `citation.py`: source reference formatting and support checks

The `Week22_Engineering/Implementation1-7` directories remain classroom experiments and are not imported by this product package.
