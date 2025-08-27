from flask import Flask
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

template_dir = BASE_DIR / "templates"
static_dir = BASE_DIR / "static"

app = Flask(__name__, template_folder=str(template_dir), static_folder=str(static_dir))

from app import routes
