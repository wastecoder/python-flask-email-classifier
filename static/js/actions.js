// Copia o conteúdo de um elemento de texto para a área de transferência e atualiza temporariamente o botão como "Copiado!"
function copyText(textoId, botaoId) {
    const texto = document.getElementById(textoId)?.innerText;
    if (!texto) return;

    navigator.clipboard.writeText(texto).then(() => {
        const btn = document.getElementById(botaoId);
        if (!btn) return;

        const oldContent = btn.innerHTML;
        btn.innerText = "Copiado!";

        setTimeout(() => {
            btn.innerHTML = oldContent;
        }, 1500);
    });
}

// Exibe uma mensagem de alerta em um contêiner específico e a oculta automaticamente após 3 segundos
function showToastError(containerId, message) {
    const container = document.getElementById(containerId);

    if (!container) return;

    // Limpa mensagens anteriores
    container.innerHTML = "";

    // Injeta o alerta
    container.innerHTML = `
        <div class="toast-notification position-fixed">
            <div class="alert alert-warning alert-dismissible show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Fechar"></button>
            </div>
        </div>
    `;

    // Oculta automaticamente após 3 segundos
    setTimeout(() => {
        container.innerHTML = "";
    }, 3000);
}

// Valida o formulário de e-mail antes do envio:
// - Garante que o usuário preencha o campo de texto ou selecione um arquivo
// - Se ambos estiverem vazios, exibe uma notificação de erro e impede o envio
function validateEmailForm(event) {
    const fileInput = document.getElementById("filesent");
    const textInput = document.getElementById("txt");

    if ((!textInput.value || textInput.value.trim() === "") &&
        (!fileInput.files || fileInput.files.length === 0)) {

        event.preventDefault(); // impede envio
        showToastError("js-error-container", "Você deve fornecer um texto ou anexar um arquivo.");
        return false;
    }

    return true;
}
