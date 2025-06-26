# embedding_utils.py

import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import pickle

DATA_DIRS = ["data/drdo_docs", "data/wikipedia_docs", "data/pdf_texts"]
FAISS_INDEX_FILE = "faiss_store/index.faiss"
FAISS_DOCS_FILE = "faiss_store/docs.pkl"

# Load embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")  # Light and fast

def get_texts():
    """
    Load all text content from .txt files in data directories.
    Returns:
        texts (List[str]), file_paths (List[str])
    """
    texts, file_paths = [], []
    for dir in DATA_DIRS:
        for fname in os.listdir(dir):
            fpath = os.path.join(dir, fname)
            if fpath.endswith(".txt"):
                with open(fpath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    texts.append(content)
                    file_paths.append(fpath)
    return texts, file_paths

def build_faiss_index():
    """
    Build FAISS index from document texts and store it along with the raw docs.
    """
    texts, paths = get_texts()
    embeddings = embedding_model.encode(texts, show_progress_bar=True)

    index = faiss.IndexFlatL2(embeddings[0].shape[0])
    index.add(np.array(embeddings))

    os.makedirs("faiss_store", exist_ok=True)
    faiss.write_index(index, FAISS_INDEX_FILE)

    with open(FAISS_DOCS_FILE, 'wb') as f:
        pickle.dump(list(zip(paths, texts)), f)

    print(f"[✔] FAISS index built and stored at: {FAISS_INDEX_FILE}")

def search_similar(query, top_k=3):
    """
    Perform semantic search over indexed documents using FAISS.

    Args:
        query (str): user input query
        top_k (int): number of top similar documents to return

    Returns:
        List[str]: top_k relevant document contents
    """
    if not os.path.exists(FAISS_INDEX_FILE) or not os.path.exists(FAISS_DOCS_FILE):
        build_faiss_index()

    index = faiss.read_index(FAISS_INDEX_FILE)
    with open(FAISS_DOCS_FILE, 'rb') as f:
        doc_data = pickle.load(f)

    query_vec = embedding_model.encode([query])
    distances, indices = index.search(np.array(query_vec), top_k)

    results = [doc_data[i][1] for i in indices[0] if i < len(doc_data)]
    return results

def load_faiss_index(index_path="faiss_store/index.faiss"):
    """
    Loads the FAISS index and the corresponding documents list.
    """
    index = faiss.read_index(index_path)
    with open("faiss_store/docs.pkl", "rb") as f:
        docs = pickle.load(f)
    return index, docs

def semantic_search(query, index, docs, model):
    """
    Performs semantic search using FAISS and returns top matching document chunks.
    """
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, k=3)  # Top 3 results
    return [docs[i][1] for i in I[0] if i < len(docs)]
