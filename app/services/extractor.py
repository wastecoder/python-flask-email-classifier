from pathlib import Path
import fitz  # PyMuPDF

def read_file(file):
    filename = file.filename
    ext = Path(filename).suffix.lower()

    if ext == '.txt':
        return file.read().decode('utf-8')

    elif ext == '.pdf':
        text = ""
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text

    else:
        return "Formato não suportado"
