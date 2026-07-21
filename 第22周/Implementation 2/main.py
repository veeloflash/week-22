import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))

try:
    import faiss
except Exception:
    faiss = None


def build_dataset():
    return [
        {"id": 1, "text": "FAISS is used for fast vector search.", "vector": [0.95, 0.10, 0.20]},
        {"id": 2, "text": "Approximate nearest neighbor methods trade precision for speed.", "vector": [0.80, 0.25, 0.10]},
        {"id": 3, "text": "Indexing allows batch retrieval over many embeddings.", "vector": [0.20, 0.85, 0.30]},
        {"id": 4, "text": "Vector databases support semantic retrieval.", "vector": [0.40, 0.70, 0.80]},
        {"id": 5, "text": "Top-K search returns the most relevant candidates.", "vector": [0.70, 0.20, 0.60]} ,
    ]


def cosine_similarity_matrix(matrix, query):
    q = np.array(query, dtype=float)
    m = np.array(matrix, dtype=float)
    qn = q / (np.linalg.norm(q) + 1e-12)
    mn = m / (np.linalg.norm(m, axis=1, keepdims=True) + 1e-12)
    return mn @ qn


def search_with_faiss(vectors, query, top_k):
    index = faiss.IndexFlatIP(len(vectors[0]))
    index.add(np.array(vectors, dtype='float32'))
    scores, ids = index.search(np.array([query], dtype='float32'), top_k)
    return [{'id': int(i), 'score': float(s)} for s, i in zip(scores[0], ids[0])]


def search_fallback(vectors, query, top_k):
    scores = cosine_similarity_matrix(vectors, query)
    order = np.argsort(scores)[::-1][:top_k]
    return [{'id': int(i + 1), 'score': float(scores[i])} for i in order]


def compare_top_k(documents, query, ks):
    vectors = [doc['vector'] for doc in documents]
    results = {}
    if faiss is not None:
        for k in ks:
            results[k] = search_with_faiss(vectors, query, k)
    else:
        for k in ks:
            results[k] = search_fallback(vectors, query, k)
    return results


def save_plot(results):
    plt.figure(figsize=(6, 4))
    x = list(results.keys())
    y = [len(results[k]) for k in x]
    plt.bar([str(v) for v in x], y, color=['#E45756', '#72B7B2', '#4E79A7'])
    plt.ylabel('Returned items')
    plt.title('Top-K comparison')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()


def main():
    documents = build_dataset()
    query = [0.90, 0.20, 0.15]
    ks = [1, 3, 5]
    results = compare_top_k(documents, query, ks)
    save_plot(results)

    with open(os.path.join(ROOT, 'dataset.json'), 'w', encoding='utf-8') as fh:
        json.dump({'query': query, 'documents': documents}, fh, indent=2)

    with open(os.path.join(ROOT, 'results.json'), 'w', encoding='utf-8') as fh:
        json.dump(results, fh, indent=2)

    report = "# Implementation 2 Testing Report\n\n"
    report += "- Built a vector index with FAISS when available, otherwise used a NumPy fallback.\n"
    report += "- Compared Top-K values 1, 3, and 5.\n"
    report += "\n## Result Summary\n"
    for k in ks:
        report += f"### Top-{k}\n"
        for item in results[k]:
            report += f"- Doc {item['id']} score={item['score']:.3f}\n"
    with open(os.path.join(ROOT, 'report.md'), 'w', encoding='utf-8') as fh:
        fh.write(report)

    print('Implementation 2 completed successfully.')


if __name__ == '__main__':
    main()
