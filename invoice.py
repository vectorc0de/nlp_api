import spacy
import pdfplumber
import re

def extract_invoice_info(pdf_path):
    nlp = spacy.load("en_core_web_trf")

    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    doc = nlp(text)

    total_amount = None
    for line in text.split('\n'):
        if "Total:" in line:
            match = re.search(r'\$(\d+\.\d+)', line)
            if match:
                total_amount = match.group(1)
                break

    description_lines = []
    start_capture = False
    for line in text.split('\n'):
        if re.match(r'Description\s+Staff Member', line, re.IGNORECASE):
            start_capture = True
            continue
        if "Subtotal:" in line:
            break
        if start_capture and line.strip():
            description_lines.append(line.strip())

    description = "\n".join(description_lines)

    return {
        "title": pdf_path.split(".")[0],
        "amount": total_amount,
        "description": description
    }