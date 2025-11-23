document.addEventListener('DOMContentLoaded', () => {
    let called = document.querySelectorAll("#called");

    for (span of called) {
        if (screen.width < 890) {
            span.id = "none";
        }

        console.log(span);
    }
})