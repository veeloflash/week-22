def build_citation(chunk: dict, citation_number: int | None = None) -> str:
    if not isinstance(chunk, dict):
        raise ValueError("Chunk must be a dictionary.")

    document_id = chunk.get("document_id", "unknown")
    filename = chunk.get("filename", "unknown")
    page = chunk.get("page", 1)
    section = chunk.get("section", "Not specified")
    chunk_id = chunk.get("chunk_id", "unknown")
    prefix = f"[{citation_number}] " if citation_number is not None else ""
    return (
        f"{prefix}Source: {filename}\n"
        f"Document: {document_id}\n"
        f"Page: {page}\n"
        f"Section: {section}\n"
        f"Chunk: {chunk_id}"
    )


def validate_answer_support(answer_text: str, sources: list) -> bool:
    if not answer_text or not sources:
        return False
    text = answer_text.lower()
    for source in sources:
        chunk_text = str(source.get("text", "")).lower()
        if chunk_text and any(token in text for token in [
            chunk_text[:20],
            source.get("filename", "").lower(),
        ]):
            return True
    return False
