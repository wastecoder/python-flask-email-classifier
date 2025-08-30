from pathlib import Path
from app.services.extractor import read_file


class MockFile:
    """Simula um arquivo enviado pelo frontend, com filename e conteúdo em bytes."""
    def __init__(self, filename, content: bytes):
        self.filename = filename
        self._content = content

    def read(self):
        return self._content


def test_extractor_read_txt_file():
    mock_file = MockFile("teste.txt", b"Conteudo do arquivo")
    result = read_file(mock_file)

    assert result == "Conteudo do arquivo"


def test_extractor_read_empty_txt_file():
    mock_file = MockFile("vazio.txt", b"")
    result = read_file(mock_file)

    assert result == ""


def test_extractor_read_pdf_file():
    path = Path("tests/fixtures/2-pages-pdf.pdf")
    with open(path, "rb") as f:
        mock_pdf = MockFile("2-pages-pdf.pdf", f.read())

    result = read_file(mock_pdf)

    assert "Primeira pagina" in result
    assert "Pagina-1" in result
    assert "Segunda pagina" in result
    assert "Pagina-2" in result
    assert "Terceira pagina" not in result
    assert "Pagina-3" not in result


def test_extractor_read_empty_pdf_file():
    path = Path("tests/fixtures/empty-pdf.pdf")
    with open(path, "rb") as f:
        mock_pdf = MockFile("empty-pdf.pdf", f.read())

    result = read_file(mock_pdf)

    assert result.strip() == ""


def test_extractor_read_unsupported_file():
    mock_file = MockFile("arquivo.docx", b"conteudo qualquer")
    result = read_file(mock_file)

    assert result == "Formato não suportado"
