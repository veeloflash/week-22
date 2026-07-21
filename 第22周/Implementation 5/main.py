import json
import os
import re
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ROOT = os.path.dirname(os.path.abspath(__file__))


def build_dataset():
    docs = [
        "RAG uses retrieval to find relevant passages before generation.",
        "Vector databases support efficient similarity search over embeddings.",
        "Transformers generate fluent text from context-rich prompts.",
        "Chunk optimization balances context length and retrieval precision.",
        "FAISS enables fast approximate nearest neighbor search at scale.",
    ]
    questions = [
        "What does RAG combine?",
        "How are vector databases used?",
        "What does FAISS help with?",
    ]
    return docs, questions


def split_into_chunks(text, size=120):
    words = re.findall(r"\w+", text)
    return [' '.join(words[i:i+size]) for i in range(0, len(words), size)]


def build_retriever(docs):
    vectorizer = TfidfVectorizer(stop_words='english')
    vectors = vectorizer.fit_transform(docs)
    return vectorizer, vectors


def answer_question(question, docs, vectorizer, vectors):
    q_vector = vectorizer.transform([question])
    scores = cosine_similarity(q_vector, vectors).ravel()
    top_idx = int(np.argmax(scores))
    context = docs[top_idx]
    answer = f"Based on the retrieved context: {context}"
    return top_idx, float(scores[top_idx]), context, answer


def save_plot(results):
    plt.figure(figsize=(6, 4))
    plt.bar([f"Q{i+1}" for i in range(len(results))], [r[1] for r in results], color=['#2F4B7C', '#FFA600', '#D45087'])
    plt.ylabel('Similarity')
    plt.title('Mini RAG retrieval scores')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()


def main():
    docs, questions = build_dataset()
    vectorizer, vectors = build_retriever(docs)
    results = []
    for question in questions:
        top_idx, score, context, answer = answer_question(question, docs, vectorizer, vectors)
        results.append({'question': question, 'top_doc_id': top_idx + 1, 'score': score, 'context': context, 'answer': answer})
    save_plot([(r['top_doc_id'], r['score']) for r in results])

    with open(os.path.join(ROOT, 'dataset.json'), 'w', encoding='utf-8') as fh:
        json.dump({'documents': docs, 'questions': questions}, fh, indent=2)

    with open(os.path.join(ROOT, 'results.json'), 'w', encoding='utf-8') as fh:
        json.dump(results, fh, indent=2)

    report = "# Implementation 5 Testing Report\n\n"
    report += "- Built a mini RAG pipeline with document retrieval and answer generation.\n"
    report += "- Used TF-IDF retrieval to select context and then produced a grounded answer.\n"
    report += "\n## Query Results\n"
    for item in results:
        report += f"- Q: {item['question']} -> Doc {item['top_doc_id']} score={item['score']:.3f}\n"
    with open(os.path.join(ROOT, 'report.md'), 'w', encoding='utf-8') as fh:
        fh.write(report)

    print('Implementation 5 completed successfully.')


if __name__ == '__main__':
    main()
