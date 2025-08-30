"""
Módulo responsável pelo pré-processamento de texto para análise com NLP.

Este módulo realiza:
- Normalização (conversão para minúsculas)
- Remoção de caracteres especiais
- Lematização com spaCy
- Remoção de stopwords e pontuação

Utiliza o modelo spaCy `pt_core_news_sm`, treinado para a língua portuguesa.

O resultado é uma string limpa, lematizada e pronta para classificação ou outras tarefas de NLP.
"""

import re
import spacy
from spacy.lang.pt.stop_words import STOP_WORDS

nlp = spacy.load("pt_core_news_sm")

def preprocess_text(text):
    """
    Realiza o pré-processamento de uma string textual para uso em tarefas de NLP.

    Este processamento assume que o texto está em português e utiliza o modelo `pt_core_news_sm` do spaCy.

    Etapas aplicadas:
        - Converte o texto para letras minúsculas.
        - Remove todos os caracteres que não sejam letras ou espaços.
        - Aplica lematização usando o modelo de linguagem.
        - Remove stopwords, pontuação e espaços vazios.
        - Junta os tokens processados novamente em uma única string.

    Parâmetros:
        text (str): Texto de entrada a ser processado.

    Retorna:
        str: Texto processado, após os tokens serem lematizados e filtrados.
    """

    text = text.lower()

    text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text)

    doc = nlp(text)

    lemmatized_tokens = [
        token.lemma_ for token in doc
        if token.text not in STOP_WORDS and not token.is_punct and not token.is_space
    ]

    return ' '.join(lemmatized_tokens)
