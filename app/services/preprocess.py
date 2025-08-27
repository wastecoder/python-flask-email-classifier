import re
import spacy
from spacy.lang.pt.stop_words import STOP_WORDS

# Carrega o modelo em português
nlp = spacy.load("pt_core_news_sm")

def preprocess_text(text):
    # 1. Colocar tudo em minúsculas
    text = text.lower()

    # 2. Manter apenas letras e espaços
    text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text)

    # 3. Processar com spaCy
    doc = nlp(text)

    # 4. Lematizar e remover stopwords
    lemmatized_tokens = [
        token.lemma_ for token in doc
        if token.text not in STOP_WORDS and not token.is_punct and not token.is_space
    ]

    # 5. Juntar novamente em string
    return ' '.join(lemmatized_tokens)
