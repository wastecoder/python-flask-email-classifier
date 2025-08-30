"""
Módulo responsável por extrair o conteúdo textual de arquivos enviados pelo frontend.

Atualmente, este módulo suporta os seguintes formatos:
- .txt: realiza leitura direta e decodificação UTF-8.
- .pdf: utiliza a biblioteca PyMuPDF (fitz) para extrair o texto de cada página.

O texto extraído é utilizado nas etapas posteriores de processamento e classificação por NLP.
"""

from pathlib import Path
import fitz  # PyMuPDF

def read_file(file):
    """
    Extrai o conteúdo textual de um arquivo .txt ou .pdf enviado via upload.

    Parâmetros:
        file: Objeto de arquivo contendo o nome e o conteúdo do arquivo.

    Retorna:
        str: Texto extraído do arquivo.

    Observações:
        - Arquivos .txt são lidos e decodificados como UTF-8.
        - Arquivos .pdf são processados com a biblioteca PyMuPDF (fitz).
        - Caso o formato não seja suportado, retorna a string "Formato não suportado".
    """

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
