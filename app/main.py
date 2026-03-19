import fitz # type: ignore
from pathlib import Path

def pdf_to_text(start_page:int, end_page:int, input_pdf_path:str, output_text_path:str):
    doc = fitz.open(input_pdf_path)
    total = doc.page_count
    if not (1 <= start_page <= end_page <= total):
        raise ValueError(f"Range must be within 1–{total}")

    # need to add checks to the input and output paths here.
    
    with open(output_text_path, "w") as f:
        for i in range(start_page - 1, end_page):
            text = doc[i].get_text("text")
            if text.strip():
                f.write(f"{text}\n\n")
    doc.close()
    return output_text_path

def main():
    start = int(input("Start page: "))
    end = int(input("End page: "))
    output_path = pdf_to_text(start_page=start, end_page=end, input_pdf_path="",output_text_path="")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    main()
