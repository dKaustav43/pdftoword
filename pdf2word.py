import pdfplumber
from docx import Document

'''

The following code takes a pdf as an input and converts to a docx file.
Input the path to your pdf file into pdf_file. 
Imput the path where you would like to store the converted text file. 

'''

pdf_file = "git_intro.pdf"
docx_file = "converted_git_into.docx"

doc = Document()

with pdfplumber.open(pdf_file) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            doc.add_paragraph(f"--- Page {i+1} ---")
            doc.add_paragraph(text)

doc.save(docx_file)
