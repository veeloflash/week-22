import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))


def cosine_similarity(a, b):
    a = np.array(a, dtype=float)
    b = np.array(b, dtype=float)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if denom == 0:
        return 0.0
    return float(np.dot(a, b) / denom)


def build_dataset():
    documents = [
        {"id": 1, "text": "Vector databases store embeddings for fast similarity search.", "vector": [0.9, 0.1, 0.2]},
        {"id": 2, "text": "FAISS supports efficient nearest-neighbor indexing.", "vector": [0.8, 0.3, 0.1]},
        {"id": 3, "text": "Chunking improves retrieval quality for long documents.", "vector": [0.1, 0.8, 0.3]},
        {"id": 4, "text": "Semantic search ranks passages by meaning rather than keywords.", "vector": [0.2, 0.7, 0.8]},
        {"id": 5, "text": "RAG combines retrieval and generation for grounded answers.", "vector": [0.3, 0.2, 0.9]},
        {"id": 6, "text": "Embedding models convert text into numerical vectors.", "vector": [0.4, 0.6, 0.5]},
    ]
    return documents


def search_top_k(documents, query_vector, top_k=3):
    scored = []
    for doc in documents:
        score = cosine_similarity(doc["vector"], query_vector)
        scored.append((score, doc))
    scored.sort(reverse=True)
    return scored[:top_k]


def save_plot(results):
    scores = [item[0] for item in results]
    labels = [f"Doc {item[1]['id']}" for item in results]
    plt.figure(figsize=(6, 4))
    plt.bar(labels, scores, color=['#4C78A8', '#F58518', '#54A24B'])
    plt.ylabel('Cosine similarity')
    plt.title('Top-K retrieval results')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()


def main():
    documents = build_dataset()
    query_vector = [0.85, 0.25, 0.15]
    results = search_top_k(documents, query_vector, top_k=3)
    save_plot(results)

    with open(os.path.join(ROOT, 'dataset.json'), 'w', encoding='utf-8') as fh:
        json.dump({'query_vector': query_vector, 'documents': documents}, fh, indent=2)

    with open(os.path.join(ROOT, 'results.json'), 'w', encoding='utf-8') as fh:
        json.dump([{'score': score, 'id': doc['id'], 'text': doc['text']} for score, doc in results], fh, indent=2)

    report = "# Implementation 1 Testing Report\n\n"
    report += "- Built a simple vector database using cosine similarity.\n"
    report += "- Stored six document vectors and executed a Top-K search.\n"
    report += "- Screenshot saved as screenshot.png.\n"
    report += "\n## Result Summary\n"
    for score, doc in results:
        report += f"- Document {doc['id']}: {doc['text']} (score={score:.3f})\n"
    with open(os.path.join(ROOT, 'report.md'), 'w', encoding='utf-8') as fh:
        fh.write(report)

    print('Implementation 1 completed successfully.')


if __name__ == '__main__':
    main()
