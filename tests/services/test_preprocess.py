from app.services.preprocess import preprocess_text


def test_preprocess_normal_portuguese_text():
    text = "O cliente solicitou o bloqueio do cartão."
    result = preprocess_text(text)

    assert "cliente" in result
    assert "solicitar" in result
    assert "bloqueio" in result
    assert "cartão" in result


def test_preprocess_text_with_punctuation():
    text = "Olá!!! Você pode, por favor, enviar o extrato?"
    result = preprocess_text(text)

    assert "olá" in result
    assert "enviar" in result
    assert "extrato" in result
    assert "!" not in result
    assert "?" not in result
    assert "," not in result


def test_preprocess_text_with_special_characters_and_numbers():
    text = "Minha senha é 1234@# e não funciona."
    result = preprocess_text(text)

    assert "senha" in result
    assert "funcionar" in result
    assert "1234" not in result
    assert "@" not in result
    assert "#" not in result


def test_preprocess_text_with_repeated_words_and_stopwords():
    text = "O cliente o cliente deseja atualizar atualizar cadastro."
    result = preprocess_text(text)
    tokens = result.split()

    assert "desejar" in tokens
    assert tokens.count("cliente") == 2
    assert tokens.count("atualizar") == 2
    assert "o" not in tokens


def test_preprocess_text_with_mixed_case():
    text = "O Cliente Deseja Atualizar Cadastro"
    result = preprocess_text(text)
    tokens = result.split()

    assert "cliente" in tokens
    assert "desejar" in tokens
    assert "atualizar" in tokens
    assert "cadastro" in tokens
    for token in tokens:
        assert token.islower()


def test_preprocess_text_with_extra_spaces():
    text = "  O   cliente   deseja   atualizar   cadastro.  "
    result = preprocess_text(text)
    tokens = result.split()

    assert "cliente" in tokens
    assert "desejar" in tokens
    assert "atualizar" in tokens
    assert "cadastro" in tokens
    assert "" not in tokens


def test_preprocess_text_with_accentuation():
    text = "Coração, ação, aviação e razão"
    result = preprocess_text(text)
    tokens = result.split()

    assert "coração" in tokens
    assert "ação" in tokens
    assert "aviação" in tokens
    assert "razão" in tokens


def test_preprocess_text_with_only_stopwords():
    text = "e o a os um uma de do da em para com sem"
    result = preprocess_text(text)
    tokens = result.split()

    assert tokens == []
