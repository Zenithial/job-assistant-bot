from pypdf import PdfReader

def parsePDF(document):
    reader = PdfReader(document)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    
    return text