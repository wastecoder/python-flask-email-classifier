"""
Inicializa a aplicação Flask e configura os diretórios de templates e arquivos estáticos.

Este módulo é responsável por:
- Criar a instância principal da aplicação (`app`)
- Definir os diretórios base, de templates e estáticos
- Importar e registrar as rotas da aplicação
"""

from flask import Flask
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

template_dir = BASE_DIR / "templates"
static_dir = BASE_DIR / "static"

app = Flask(__name__, template_folder=str(template_dir), static_folder=str(static_dir))

from app import routes
