import fitz # type: ignore
from pathlib import Path

def pdf_to_text(start, end, input_pdf_path:str = "data/pdfs/2025-HVM-Catapult-annual-report.pdf", output_text_path:str = "data/output_txts/exp3.txt"):
    doc = fitz.open(input_pdf_path)
    total = doc.page_count
    if not (1 <= start <= end <= total):
        raise ValueError(f"Range must be within 1–{total}")

    #Path(output_text_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_text_path, "w") as f:
        for i in range(start - 1, end):
            text = doc[i].get_text("text")
            if text.strip():
                f.write(f"--- Page {i+1} ---\n{text}\n\n")

    doc.close()
    return output_text_path

def main():
    start = int(input("Start page: "))
    end = int(input("End page: "))
    print(f"Saved to: {pdf_to_text(start, end)}")

if __name__ == "__main__":
    main()