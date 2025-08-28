document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("copiarBtn")?.addEventListener("click", () => {
        const texto = document.getElementById("respostaTexto")?.innerText;
        if (!texto) return;

        navigator.clipboard.writeText(texto).then(() => {
            const btn = document.getElementById("copiarBtn");
            btn.innerText = "Copiado!";
            setTimeout(() => {
                btn.innerHTML = '<i class="fas fa-copy"></i>';
            }, 1500);
        });
    });
});
