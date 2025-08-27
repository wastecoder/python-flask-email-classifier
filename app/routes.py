from app import app
from flask import render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email-form')
def email_form():
    return render_template('email-form.html')

@app.route('/process', methods=['POST'])
def process_email():
    return "Processamento futuro..."
