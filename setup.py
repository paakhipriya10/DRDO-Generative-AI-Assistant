# setup.py
from pdf_handler import process_all_pdfs
from embedding_utils import build_faiss_index

process_all_pdfs()
build_faiss_index()
