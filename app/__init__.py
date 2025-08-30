"""
Inicializa a aplicação Flask e configura os diretórios de templates e arquivos estáticos.

Este módulo é responsável por:
- Criar a instância principal da aplicação (`app`)
- Definir os diretórios base, de templates e estáticos
- Importar e registrar as rotas da aplicação
"""

from flask import Flask, render_template
from pathlib import Path
from werkzeug.exceptions import RequestEntityTooLarge

BASE_DIR = Path(__file__).resolve().parent.parent

template_dir = BASE_DIR / "templates"
static_dir = BASE_DIR / "static"

app = Flask(__name__, template_folder=str(template_dir), static_folder=str(static_dir))

MAX_UPLOAD_SIZE_MB = 5
app.config['MAX_CONTENT_LENGTH'] = MAX_UPLOAD_SIZE_MB * 1024 * 1024

# Tratamento de erro para arquivos acima do limite máximo
@app.errorhandler(RequestEntityTooLarge)
def handle_large_file(e):
    return render_template(
        'email/email-page.html',
        error_message=f'Arquivo muito grande. Tamanho máximo permitido: {MAX_UPLOAD_SIZE_MB} MB'
    ), 413

from app import routes
