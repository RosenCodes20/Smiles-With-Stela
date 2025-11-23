document.addEventListener('DOMContentLoaded', () => {
    let a = document.querySelectorAll('.nav a');

    for (let link of a) {
        link.addEventListener('click', () => {
            document.querySelector('[type="checkbox"]').checked = false;
        })
    }
})