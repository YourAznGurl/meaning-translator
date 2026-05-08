function translateText() {
    const text = document.getElementById("inputText").value;
    const sourceLang = document.getElementById("sourceLang").value;
    const targetLang = document.getElementById("targetLang").value;

    fetch("http://localhost:5000/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            text: text,
            source_lang: sourceLang,
            target_lang: targetLang
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("output").innerHTML = `
            <h3>Meaning:</h3> ${data.meaning}<br><br>
            <h3>Translation:</h3> ${data.translation}<br><br>
            <h3>Explanation:</h3> ${data.explanation}
        `;
    });
}

document.getElementById("themeSelector").addEventListener("change", function() {
    const theme = this.value;
    document.getElementById("themeStylesheet").href = `styles/${theme}.css`;
});
