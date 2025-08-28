import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MAX_OUTPUT_TOKENS = 200

def classificar_email(texto: str) -> dict:
    prompt = (
        "Você é um assistente de atendimento automatizado para uma empresa do setor financeiro.\n\n"
        "Classifique o e-mail abaixo como 'Produtivo' ou 'Improdutivo'.\n"
        "- Considere como **Produtivo** se o e-mail requer uma ação ou resposta específica (ex.: dúvidas, solicitações, atualizações de casos).\n"
        "- Considere como **Improdutivo** se não exige ação imediata (ex.: agradecimentos, felicitações).\n\n"
        "Depois, gere uma resposta automática apropriada.\n\n"
        "Responda em JSON no formato (sem markdown):\n"
        "{\n"
        "  \"categoria\": \"Produtivo ou Improdutivo\",\n"
        "  \"resposta\": \"Texto da resposta\"\n"
        "}\n\n"
        f"E-mail:\n{texto}"
    )

    try:
        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt,
            max_output_tokens=MAX_OUTPUT_TOKENS,
            temperature=0.3
        )

        content = response.output_text.strip()
        print("Resposta bruta da API:\n", content)

        try:
            resultado = json.loads(content)
        except json.JSONDecodeError:
            categoria, resposta = None, ""
            for linha in content.splitlines():
                if linha.lower().startswith("categoria:"):
                    categoria = linha.split(":", 1)[1].strip()
                elif linha.lower().startswith("resposta:"):
                    resposta = linha.split(":", 1)[1].strip()
                elif resposta:
                    resposta += " " + linha.strip()

            resultado = {
                "categoria": categoria or "Indefinido",
                "resposta": resposta or content
            }

        return {
            "categoria": resultado.get("categoria", "Indefinido"),
            "resposta": resultado.get("resposta", "")
        }

    except Exception as e:
        print("Erro ao classificar:", e)
        return {
            "categoria": "Erro",
            "resposta": "Não foi possível gerar uma resposta no momento."
        }
