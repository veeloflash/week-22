from sentence_transformers import SentenceTransformer
import numpy as np

class MiniRAG:
    def __init__(self, llm):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.llm = llm
        self.texts = []
        self.vectors = []

    def add_docs(self, docs):
        self.texts.extend(docs)
        vecs = self.model.encode(docs)
        self.vectors.extend(vecs)

    def retrieve(self, query, top_k=3):
        q_vec = self.model.encode([query])[0]
        scores = np.dot(self.vectors, q_vec)
        idx = np.argsort(scores)[::-1][:top_k]
        return [self.texts[i] for i in idx]

    def answer(self, query):
        context = "\n".join(self.retrieve(query))
        prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
        return self.llm(prompt)


def fake_llm(prompt):
    return "This is a fake LLM answer based on context."

if __name__ == "__main__":
    rag = MiniRAG(fake_llm)
    docs = ["Python is a programming language.", "Java is used for backend.", "AI uses embeddings."]
    rag.add_docs(docs)

    print(rag.answer("What is Python?"))
