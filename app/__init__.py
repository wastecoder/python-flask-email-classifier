from flask import Flask
from pathlib import Path

template_dir = Path(__file__).resolve().parent.parent / "templates"
app = Flask(__name__, template_folder=str(template_dir))

from app import routes
