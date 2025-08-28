import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MAX_OUTPUT_TOKENS = 200

def classificar_email(texto: str) -> dict:
    messages = [
        {
            "role": "system",
            "content": "Você é um assistente de atendimento automatizado para uma empresa do setor financeiro.\n\n"
                "Classifique o e-mail como 'Produtivo' ou 'Improdutivo'.\n"
                "- Produtivo: requer uma ação ou resposta específica (ex.: dúvidas, solicitações, atualizações de casos).\n"
                "- Improdutivo: não exige ação imediata (ex.: agradecimentos, felicitações).\n\n"
                "Depois, gere uma resposta automática apropriada.\n\n"
                "Retorne APENAS em JSON no formato:\n"
                "{\n"
                "  \"categoria\": \"Produtivo ou Improdutivo\",\n"
                "  \"resposta\": \"Texto da resposta\"\n"
                "}"
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
            "categoria": result.get("categoria", "Indefinido"),
            "resposta": result.get("resposta", "")
        }

    except Exception as e:
        print("Erro ao classificar:", e)
        return {
            "categoria": "Erro",
            "resposta": "Não foi possível gerar uma resposta no momento."
        }
