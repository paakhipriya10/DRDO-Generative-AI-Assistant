# agent_core.py

import os
from typing import List
from embedding_utils import load_faiss_index, search_similar
from summarizer import summarize_text
from pdf_handler import extract_text_from_pdf
from transformers import pipeline

# Load Hugging Face QA pipeline
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Load FAISS index on startup
faiss_index, id_to_doc_map = load_faiss_index()

def generate_answer_from_context(question: str, context: str) -> str:
    try:
        result = qa_pipeline(question=question, context=context[:512])  # limit context
        return result.get("answer", "")
    except Exception as e:
        return f"Error during Q/A: {e}"

def process_query(question: str) -> str:
    print(f"[Query] {question}")

    # Step 1: Semantic Search
    matched_chunks = search_similar(question, top_k=5)
    print("\n[Matched Chunks]")
    for i, chunk in enumerate(matched_chunks):
        print(f"Chunk {i+1}:\n{chunk[:300]}\n---")

    if matched_chunks:
        combined_context = " ".join(matched_chunks)
        answer = generate_answer_from_context(question, combined_context)

        # Step 2: Summarize if too long
        if len(answer.split()) > 100:
            return summarize_text(answer)

        if answer.strip():
            return answer

    # Step 3: Keyword Search fallback
    print("[Fallback] No semantic match found, trying keyword search.")
    for folder in ['data/drdo_docs/', 'data/wikipedia_docs/']:
        for file in os.listdir(folder):
            if file.endswith(".txt"):
                with open(os.path.join(folder, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    if any(word.lower() in content.lower() for word in question.split()):
                        snippet = summarize_text(content)
                        return snippet or "Found related content but couldn't summarize well."

    return "Sorry, I couldn't find relevant information."

def summarize_pdf(path: str) -> str:
    pdf_text = extract_text_from_pdf(path)
    if not pdf_text:
        return "Failed to extract text from the PDF."
    return summarize_text(pdf_text)
