"""Product vector database API.

The implementation is kept in the product module at the package root for
backwards compatibility with the existing product tests; this is the public
import path used by product integrations.
"""

from vector_database import VectorDatabase

__all__ = ["VectorDatabase"]
