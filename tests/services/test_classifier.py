import json
from unittest.mock import patch, MagicMock
from app.services.classifier import classify_email


def test_classify_productive_email_block_card_request():
    # Simula a resposta da API da OpenAI
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content=json.dumps({
            "category": "Produtivo",
            "answer": "Registramos sua solicitação de bloqueio do cartão e estamos processando o pedido."
        })))
    ]

    # Substitui a chamada real por um mock
    with patch("app.services.classifier.client.chat.completions.create", return_value=mock_response):
        resultado = classify_email("Quero bloquear meu cartão de crédito.")

    assert resultado["category"] == "Produtivo"
    assert resultado["answer"].startswith("Registramos sua solicitação")
    assert "category" in resultado
    assert "answer" in resultado


def test_classify_unproductive_email_team_greeting():
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content=json.dumps({
            "category": "Improdutivo",
            "answer": "Obrigado pelo contato! Tenha um ótimo dia."
        })))
    ]

    with patch("app.services.classifier.client.chat.completions.create", return_value=mock_response):
        resultado = classify_email("Feliz aniversário para toda a equipe!")

    assert resultado["category"] == "Improdutivo"
    assert resultado["answer"].startswith("Obrigado pelo contato")
    assert "category" in resultado
    assert "answer" in resultado


def test_classify_email_api_failure():
    with patch("app.services.classifier.client.chat.completions.create", side_effect=Exception("Falha na API")):
        resultado = classify_email("Teste de erro")

    assert resultado["category"] == "Erro"
    assert resultado["answer"].startswith("Não foi possível")
    assert "category" in resultado
    assert "answer" in resultado


def test_classify_email_empty_input():
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content=json.dumps({
            "category": "Improdutivo",
            "answer": "Não identificamos conteúdo na sua mensagem. Por favor, envie novamente."
        })))
    ]

    with patch("app.services.classifier.client.chat.completions.create", return_value=mock_response):
        resultado = classify_email("")

    assert resultado["category"] == "Improdutivo"
    assert resultado["answer"].startswith("Não identificamos conteúdo na sua mensagem.")


def test_classify_email_invalid_json():
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content="isto_nao_e_json"))
    ]

    with patch("app.services.classifier.client.chat.completions.create", return_value=mock_response):
        resultado = classify_email("Teste de JSON inválido")

    assert resultado["category"] == "Erro"
    assert resultado["answer"].startswith("Não foi possível")


def test_classify_email_missing_fields():
    mock_response = MagicMock()
    mock_response.choices = [
        MagicMock(message=MagicMock(content=json.dumps({})))
    ]

    with patch("app.services.classifier.client.chat.completions.create", return_value=mock_response):
        resultado = classify_email("Solicito extrato da minha conta.")

    assert resultado["category"] == "Indefinido"
    assert resultado["answer"] == ""
