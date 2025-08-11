# Retriever skeleton: embeddings -> FAISS
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class Retriever:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.embedder = SentenceTransformer(model_name)
        self.index = None

    def build_index(self, docs):
        embs = self.embedder.encode(docs, convert_to_numpy=True)
        dim = embs.shape[1]
        self.index = faiss.IndexFlatL2(dim)
        self.index.add(embs)

    def query(self, q, k=5):
        v = self.embedder.encode([q], convert_to_numpy=True)
        D, I = self.index.search(v, k)
        return I[0].tolist()
