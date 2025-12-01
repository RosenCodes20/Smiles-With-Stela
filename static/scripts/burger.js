document.addEventListener('DOMContentLoaded', () => {
    let a = document.querySelectorAll('.nav a');

    for (let link of a) {
        if (link.id !== "search-icon") {
             link.addEventListener('click', () => {
                document.querySelector('[type="checkbox"]').checked = false;
            })
        }
    }
})