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
