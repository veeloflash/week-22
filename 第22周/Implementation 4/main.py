import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = os.path.dirname(os.path.abspath(__file__))


def build_documents():
    return [
        "Semantic retrieval uses embeddings to find passages by meaning.",
        "Ranking orders candidates by relevance to the user query.",
        "A retrieval engine compares query vectors against document vectors.",
        "Keyword search is often less robust than semantic matching.",
        "Dense retrieval improves recall for paraphrased questions.",
    ]


def semantic_search(documents, query, top_k=3):
    vectorizer = TfidfVectorizer(stop_words='english')
    matrix = vectorizer.fit_transform(documents + [query])
    query_vector = matrix[-1]
    doc_vectors = matrix[:-1]
    scores = cosine_similarity(doc_vectors, query_vector).ravel()
    ranked = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)
    return [(idx, float(score)) for idx, score in ranked[:top_k]]


def compare_methods(documents, query):
    keyword_hits = []
    for idx, doc in enumerate(documents):
        if any(word in doc.lower() for word in query.lower().split()):
            keyword_hits.append(idx)
    semantic = semantic_search(documents, query, top_k=3)
    return {'keyword_hits': keyword_hits, 'semantic_results': semantic}


def save_plot(scores):
    plt.figure(figsize=(6, 4))
    plt.bar([f"Doc {i+1}" for i, _ in scores], [s for _, s in scores], color=['#76B7B2', '#E15759', '#4E79A7'])
    plt.ylabel('Similarity score')
    plt.title('Semantic retrieval ranking')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()


def main():
    documents = build_documents()
    query = "How does semantic retrieval work?"
    results = semantic_search(documents, query, top_k=3)
    save_plot(results)

    with open(os.path.join(ROOT, 'dataset.json'), 'w', encoding='utf-8') as fh:
        json.dump({'query': query, 'documents': documents}, fh, indent=2)

    with open(os.path.join(ROOT, 'results.json'), 'w', encoding='utf-8') as fh:
        json.dump({'semantic_results': [{'doc_id': idx + 1, 'score': score} for idx, score in results], 'comparison': compare_methods(documents, query)}, fh, indent=2)

    report = "# Implementation 4 Testing Report\n\n"
    report += "- Implemented embedding retrieval using TF-IDF vectors.\n"
    report += "- Ranked documents by cosine similarity and compared the results with a simple keyword baseline.\n"
    report += "\n## Top Results\n"
    for idx, score in results:
        report += f"- Document {idx + 1}: score={score:.3f}\n"
    with open(os.path.join(ROOT, 'report.md'), 'w', encoding='utf-8') as fh:
        fh.write(report)

    print('Implementation 4 completed successfully.')


if __name__ == '__main__':
    main()
