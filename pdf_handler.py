# pdf_handler.py

import os
import PyPDF2

PDF_DIR = "data/pdfs"
OUTPUT_DIR = "data/pdf_texts"

def extract_text_from_pdf(pdf_path):
    """
    Extract raw text from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file.
    
    Returns:
        str: Extracted text.
    """
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

def process_all_pdfs():
    """
    Extracts text from all PDFs in PDF_DIR and saves them as .txt files in OUTPUT_DIR.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    for filename in os.listdir(PDF_DIR):
        if filename.endswith(".pdf"):
            pdf_path = os.path.join(PDF_DIR, filename)
            txt_filename = os.path.splitext(filename)[0] + ".txt"
            output_path = os.path.join(OUTPUT_DIR, txt_filename)

            if not os.path.exists(output_path):
                print(f"[⇨] Extracting text from {filename}...")
                text = extract_text_from_pdf(pdf_path)
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"[✔] Saved extracted text to {output_path}")
