import pandas as pd
import fitz

# parser.py: This file contains a function parser_pdf that takes a PDF file path, 
# opens it using fitz (PyMuPDF), extracts text from all pages,
# and returns the concatenated text.
 
def parser_pdf(file_path):
    pdf = fitz.open(file_path)
    text = "\n".join([page.get_text() for page in pdf ])
    return text