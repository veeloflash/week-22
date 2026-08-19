from flask import Flask, request, render_template, jsonify
from src.rag import KnowledgeBaseRAG
from src.upload import UploadManager
from security.sanitizer import PromptInjectionFilter, ensure_upload_dir
from security.permissions_advanced import Permission
import logging

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10MB limit
rag_system = KnowledgeBaseRAG()
uploader = UploadManager(rag_system)
prompt_filter = PromptInjectionFilter()
ensure_upload_dir()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template(
        "index.html",
        answer=None,
        sources=[],
        citations=[],
        retrieval_method=rag_system.retrieval_method,
        generation_mode=rag_system.generation_mode,
        document_count=len(rag_system.documents),
        upload_result=None,
    )

@app.route("/upload", methods=["POST"])
def upload():
    try:
        f = request.files.get("file")
        user_id = request.form.get("user_id", "anonymous")
        user_role = request.form.get("user_role", "student")
        subject = request.form.get("subject", "")
        grade = request.form.get("grade", "")
        class_id = request.form.get("class_id", "")
        private = request.form.get("private", "false").lower() == "true"
        
        if not f or f.filename == "":
            return jsonify({"error": "No file provided"}), 400
        
        # Security: validate file before processing
        from security.sanitizer import validate_upload_file, sanitize_filename
        is_valid, error_msg = validate_upload_file(f.filename, f.content_type, len(f.read()))
        f.seek(0)  # Reset file pointer
        
        if not is_valid:
            return jsonify({"error": error_msg}), 400
        
        # Sanitize filename
        safe_filename = sanitize_filename(f.filename)
        f.filename = safe_filename
        
        # Prepare metadata with permissions
        metadata_base = {
            "subject": subject,
            "grade": grade,
            "user_role": user_role,
        }
        
        # Add permission metadata
        Permission.add_permission(
            metadata_base,
            owner_id=user_id,
            allowed_roles=["student", "teacher"] if user_role == "teacher" else ["student"],
            class_id=class_id if class_id else None,
            private=private
        )
        
        result = uploader.upload_file(f, user_role=user_role, metadata_base=metadata_base)
        logger.info(f"File uploaded: {safe_filename} by {user_id}")
        
        response = {
            "status": "success",
            "document_id": result["document_id"],
            "filename": result["filename"],
            "chunk_count": result["chunk_count"],
            "pages": result.get("pages", 1)
        }
        if request.accept_mimetypes.best == "application/json":
            return jsonify(response)
        return render_template(
            "index.html",
            answer=None,
            sources=[],
            citations=[],
            retrieval_method=rag_system.retrieval_method,
            generation_mode=rag_system.generation_mode,
            document_count=len(rag_system.documents),
            upload_result=response,
        )
    except ValueError as e:
        logger.warning(f"Validation error: {str(e)}")
        if request.accept_mimetypes.best != "application/json":
            return render_template(
                "index.html",
                answer=None,
                sources=[],
                citations=[],
                retrieval_method=rag_system.retrieval_method,
                generation_mode=rag_system.generation_mode,
                document_count=len(rag_system.documents),
                error=str(e),
                upload_result=None,
            ), 400
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return jsonify({"error": f"Upload failed: {str(e)}"}), 500

@app.route("/ask", methods=["POST"])
def ask():
    try:
        q = request.form.get("question", "")
        user_id = request.form.get("user_id", "anonymous")
        user_role = request.form.get("user_role", "student")
        top_k = int(request.form.get("top_k", "5"))
        
        if not q or not q.strip():
            return jsonify({"error": "Question cannot be empty"}), 400
        
        # Security: check for prompt injection
        is_safe, threat_msg = prompt_filter.is_safe(q)
        if not is_safe:
            logger.warning(f"Potential injection from {user_id}: {threat_msg}")
            return jsonify({"error": "Question contains potentially malicious content"}), 400
        
        # Process question through RAG with permission checking
        result = rag_system.answer(
            q, 
            user_id=user_id,
            user_role=user_role, 
            top_k=top_k,
            permission_checker=lambda meta: Permission.can_access(user_id, user_role, meta)
        )
        
        logger.info(f"Question answered for {user_id}: {q[:50]}...")
        return render_template(
            "index.html",
            answer=result["answer"],
            sources=result["sources"],
            citations=result["citations"],
            retrieval_method=result["retrieval_method"],
            generation_mode=result["generation_mode"],
            document_count=len(rag_system.documents),
        )
    except Exception as e:
        logger.error(f"Question processing error: {str(e)}")
        return jsonify({"error": f"Question processing failed: {str(e)}"}), 500

if __name__ == "__main__":
    # Production: disable debug mode
    # Development: set DEBUG=true environment variable
    import os
    debug_mode = os.getenv("DEBUG", "false").lower() == "true"
    app.run(debug=debug_mode, host="127.0.0.1", port=5000)