"""Product acceptance tests for the upload-to-index pipeline and citations."""

from io import BytesIO
from pathlib import Path

from werkzeug.datastructures import FileStorage

from citation import build_citation
from upload import UploadManager


class FakeRAG:
    def __init__(self):
        self.documents = []
        self.hashes = set()
        self.indexed_metadata = []

    def add_documents(self, documents, metadata):
        self.documents.extend(documents)
        self.indexed_metadata.extend(metadata)


def make_upload(name, content, mimetype):
    return FileStorage(
        stream=BytesIO(content),
        filename=name,
        content_type=mimetype,
    )


def test_txt_upload_reaches_index(tmp_path):
    rag = FakeRAG()
    result = UploadManager(rag, upload_dir=str(tmp_path)).upload_file(
        make_upload("notes.txt", b"Newton's first law describes inertia.", "text/plain")
    )
    assert result["chunk_count"] >= 1
    assert rag.indexed_metadata[0]["filename"] == "notes.txt"


def test_markdown_upload_reaches_index(tmp_path):
    rag = FakeRAG()
    result = UploadManager(rag, upload_dir=str(tmp_path)).upload_file(
        make_upload("notes.md", b"# Mechanics\n\nMomentum is conserved in a closed system.", "text/markdown")
    )
    assert result["chunk_count"] >= 1
    assert rag.indexed_metadata[0]["section"] == "Document body"


def test_pdf_upload_preserves_page_and_chunk_metadata(tmp_path):
    pdf_path = Path(__file__).parents[1] / "data" / "sample_physics.pdf"
    if not pdf_path.exists():
        return
    rag = FakeRAG()
    result = UploadManager(rag, upload_dir=str(tmp_path)).upload_file(
        make_upload("sample_physics.pdf", pdf_path.read_bytes(), "application/pdf")
    )
    assert result["pages"] >= 1
    assert result["chunk_count"] >= 1
    assert rag.indexed_metadata[0]["page"] >= 1
    assert rag.indexed_metadata[0]["section"] == "PDF page"


def test_citation_contains_product_acceptance_fields():
    citation = build_citation(
        {
            "document_id": "doc-0001",
            "filename": "notes.md",
            "page": 1,
            "section": "Mechanics",
            "chunk_id": "doc-0001-001",
        },
        citation_number=1,
    )
    assert "[1]" in citation
    assert "notes.md" in citation
    assert "Page: 1" in citation
    assert "Section: Mechanics" in citation
    assert "Chunk: doc-0001-001" in citation
