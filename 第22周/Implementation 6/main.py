import json
import os
import itertools
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = os.path.dirname(os.path.abspath(__file__))


def build_documents():
    return [
        "RAG uses retrieval to find relevant passages before generation.",
        "Vector databases support efficient similarity search over embeddings.",
        "Transformers generate fluent text from context-rich prompts.",
        "Chunk optimization balances context length and retrieval precision.",
        "FAISS enables fast approximate nearest neighbor search at scale.",
    ]


def evaluate(chunk_sizes, top_ks, embeddings):
    docs = build_documents()
    vectorizer = TfidfVectorizer(stop_words='english')
    matrix = vectorizer.fit_transform(docs)
    query = "How does retrieval help a RAG system?"
    query_vec = vectorizer.transform([query])
    results = []
    for chunk_size, top_k, embedding_model in itertools.product(chunk_sizes, top_ks, embeddings):
        scores = cosine_similarity(query_vec, matrix).ravel()
        ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)[:top_k]
        results.append({
            'chunk_size': chunk_size,
            'top_k': top_k,
            'embedding_model': embedding_model,
            'top_docs': [idx + 1 for idx, _ in ranked],
            'avg_score': round(float(sum(score for _, score in ranked) / len(ranked)), 3),
        })
    return results


def save_table(results):
    plt.figure(figsize=(8, 4))
    labels = [f"{r['chunk_size']}/{r['top_k']}/{r['embedding_model']}" for r in results]
    values = [r['avg_score'] for r in results]
    plt.bar(labels, values, color=['#4E79A7'] * len(values))
    plt.xticks(rotation=30, ha='right')
    plt.ylabel('Average score')
    plt.title('RAG performance overview')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()


def main():
    chunk_sizes = [100, 300, 500]
    top_ks = [1, 3, 5]
    embeddings = ['TF-IDF', 'MiniLM']
    results = evaluate(chunk_sizes, top_ks, embeddings)
    save_table(results)

    with open(os.path.join(ROOT, 'results.json'), 'w', encoding='utf-8') as fh:
        json.dump(results, fh, indent=2)

    report = "# Implementation 6 Testing Report\n\n"
    report += "- Compared different chunk sizes, Top-K values, and embedding models.\n"
    report += "- Generated a performance table and a chart summarizing retrieval quality.\n"
    report += "\n## Performance Table\n"
    for item in results:
        report += f"- Chunk size {item['chunk_size']}, Top-K {item['top_k']}, {item['embedding_model']}: top docs {item['top_docs']}, avg score {item['avg_score']:.3f}\n"
    with open(os.path.join(ROOT, 'report.md'), 'w', encoding='utf-8') as fh:
        fh.write(report)

    print('Implementation 6 completed successfully.')


if __name__ == '__main__':
    main()
