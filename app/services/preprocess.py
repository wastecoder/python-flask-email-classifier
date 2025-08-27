import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
stop_words = set(stopwords.words('portuguese'))

def preprocess_text(text):
    # 1. Colocar tudo em minúsculas
    text = text.lower()

    # 2. Manter apenas letras e espaços
    text = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', text)

    # 3. Tokenizar
    tokens = text.split()

    # 4. Remover stopwords
    cleaned_tokens = [
        word for word in tokens if word not in stop_words
    ]

    # 5. Juntar os tokens novamente em um texto
    return ' '.join(cleaned_tokens)
