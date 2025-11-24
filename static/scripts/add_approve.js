document.addEventListener('DOMContentLoaded', () => {
    let texts = document.querySelectorAll(".about-us-sect > p");

    for (let text of texts) {
        if (screen.width < 900) {
            text.textContent += " ✅";
            console.log(text);
        }
    }
})