
def extract_text_from_pdf(file_path):
    import os
   

    import pdfplumber
    text = ""

    with pdfplumber.open(file_path) as pdf:
        print(" TOTAL PAGES:", len(pdf.pages))
        for page in pdf.pages:
            page_text = page.extract_text()
            print(" PAGE TEXT:", page_text)
            if page_text:
                text += page_text + "\n"

    return text.strip()
