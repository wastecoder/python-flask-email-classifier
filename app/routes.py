from app import app
from flask import render_template, request
from app.services.extractor import read_file

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/email-form')
def email_form():
    return render_template('email-form.html')

@app.route('/process', methods=['POST'])
def process_email():
    text = request.form.get('text', '')

    if not text and 'file' in request.files:
        file = request.files['file']
        if file.filename != '':
            text = read_file(file)

    resultado = {
        'categoria': 'Produtivo',
        'resposta': 'Obrigado pelo contato! Estamos analisando sua solicitação.'
    }

    return render_template('email-form.html', resultado=resultado, texto_original=text)
