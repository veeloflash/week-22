# Product Dataset Manifest

The product dataset contains 58 document files under this directory, including the five subject seed documents, the `test_corpus/` evaluation corpus, `sample_physics.pdf`, and `sample_notes.md`.

| Format | Count | Validation path |
|---|---:|---|
| TXT | 55 | `UploadManager.upload_file` -> UTF-8 parse -> chunk -> embed -> vector index |
| Markdown | 1 | `UploadManager.upload_file` -> UTF-8 parse -> chunk -> embed -> vector index |
| PDF | 1 | `parse_pdf_with_pages` preserves page metadata before chunking |

The corpus is intentionally kept inside the Product directory and is separate from `Week22_Engineering`.

To regenerate or inspect the corpus:

```powershell
Get-ChildItem data -Recurse -File | Where-Object { $_.Extension -in '.txt','.md','.pdf' }
```
