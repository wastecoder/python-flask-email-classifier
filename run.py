"""
Ponto de entrada da aplicação Flask.

Este script inicializa o servidor de aplicação usando Waitress, adequado para ambientes de produção.

Uso:
    python run.py
"""

from waitress import serve
from app import app
import os

if __name__ == "__main__":
    app.debug = False

    port = int(os.environ.get("PORT", 5000))
    serve(app, host="0.0.0.0", port=port)
