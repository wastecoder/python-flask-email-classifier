"""
Módulo responsável por classificar e-mails recebidos por uma empresa do setor financeiro.

Este serviço utiliza a API da OpenAI para analisar o conteúdo textual de um e-mail,
classificando-o como 'Produtivo' ou 'Improdutivo', e gerando uma resposta automática adequada.

Uso típico:
    resultado = classify_email("Gostaria de atualizar meus dados cadastrais.")
"""

import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MAX_OUTPUT_TOKENS = 500

def classify_email(texto: str) -> dict:
    """
    Classifica o conteúdo de um e-mail como 'Produtivo' ou 'Improdutivo' e gera uma resposta automática.

    A classificação segue os critérios:
    - 'Produtivo': requer ação ou resposta (ex.: dúvidas, solicitações, atualizações).
    - 'Improdutivo': não exige ação (ex.: agradecimentos, felicitações).

    Parâmetros:
        texto (str): O conteúdo do e-mail a ser analisado.

    Retorna:
        dict: Um dicionário contendo:
            - "category": str - 'Produtivo', 'Improdutivo' ou 'Erro'
            - "answer": str - Resposta automática apropriada ou mensagem de erro
    """

    messages = [
        {
            "role": "system",
            "content": (
                "Você é um assistente de atendimento automatizado para uma empresa do setor financeiro.\n\n"
                "Classifique o e-mail como 'Produtivo' ou 'Improdutivo'.\n"
                "- Produtivo: requer uma ação ou resposta específica (ex.: dúvidas, solicitações, atualizações de casos).\n"
                "- Improdutivo: não exige ação imediata (ex.: agradecimentos, felicitações).\n\n"
                "Depois, gere uma resposta automática apropriada.\n\n"
                "Retorne APENAS em JSON no formato:\n"
                "{\n"
                "  \"category\": \"Produtivo ou Improdutivo\",\n"
                "  \"answer\": \"Texto da resposta\"\n"
                "}"
            )
        },
        {
            "role": "user",
            "content": f"E-mail:\n{texto}"
        }
    ]

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=MAX_OUTPUT_TOKENS,
            temperature=0.3,
            response_format={"type": "json_object"}
        )

        content = response.choices[0].message.content.strip()
        result = json.loads(content)

        return {
            "category": result.get("category", "Indefinido"),
            "answer": result.get("answer", "")
        }

    except Exception as e:
        print("Erro ao classificar:", e)
        return {
            "category": "Erro",
            "answer": "Não foi possível gerar uma resposta no momento."
        }
