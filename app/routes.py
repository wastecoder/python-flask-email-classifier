"""
Define as rotas principais da aplicação Flask.

Fluxo:
- Recebe input do usuário via formulário (texto direto ou upload de arquivo .pdf/.txt)
- Realiza extração, pré-processamento e classificação do conteúdo textual
- Renderiza a resposta ao usuário com a categoria identificada e mensagem automática

Rotas:
- `/`: Página inicial
- `/email-form`: Formulário de entrada
- `/process`: Processamento do texto enviado
"""

from app import app
from flask import render_template, request
from app.services.extractor import read_file
from app.services.preprocess import preprocess_text
from app.services.classifier import classify_email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email-form')
def email_form():
    return render_template('email/email-page.html')

@app.route('/process', methods=['POST'])
def process_email():
    """
    Processa o texto enviado pelo formulário.

    Fluxo:
    - Recebe texto diretamente (textarea) ou via upload de arquivo (PDF ou TXT)
    - Extrai o conteúdo textual (se for arquivo)
    - Aplica pré-processamento NLP
    - Classifica o conteúdo como 'Produtivo' ou 'Improdutivo'
    - Renderiza a página com o resultado da classificação
    """

    text = request.form.get('text', '')
    file = request.files.get('file')

    if not text and (not file or file.filename == ''):
        return render_template('email/email-page.html', error_message='Você deve fornecer um texto ou anexar um arquivo.')

    if not text and file and file.filename != '':
        text = read_file(file)

    clean_text = preprocess_text(text)

    result = classify_email(clean_text)

    return render_template(
        'email/email-page.html',
        result=result,
        submitted_text=text,
    )
