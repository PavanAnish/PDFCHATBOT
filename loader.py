# loader.py
import fitz  # PyMuPDF

def load_pdf_text(path):
    doc = fitz.open(path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
