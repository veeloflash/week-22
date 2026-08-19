"""Public product API for the Week 22 AI Knowledge Base Assistant.

The classroom Implementation directories are intentionally outside this package.
"""

from .rag import KnowledgeBaseRAG
from .upload import UploadManager
from .retrieval import RetrievalEngine
from .vector_database import VectorDatabase

__all__ = ["KnowledgeBaseRAG", "UploadManager", "RetrievalEngine", "VectorDatabase"]
