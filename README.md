# PDF to Text Converter

Extracts text from a PDF file into a `.txt` file, with basic multi-column support.

## Requirements
```bash
pip install pymupdf
```

## Usage

Run directly:
```bash
python app/main.py
```

You will be prompted for a start and end page number (1-indexed). 
You need to input_pdf_path and output_txt_path.

## Notes

- Page numbers are 1-indexed and inclusive on both ends.
- Multi-column layouts are handled by PyMuPDF's built-in reading-order heuristics better than pdfplumber.