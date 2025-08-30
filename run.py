"""
Ponto de entrada da aplicação Flask.

Este script inicializa o servidor de aplicação usando Waitress, adequado para ambientes de produção.

Uso:
    python run.py
"""

from waitress import serve
from app import app

if __name__ == "__main__":
    app.debug = False

    serve(app, host="0.0.0.0", port=5000)
