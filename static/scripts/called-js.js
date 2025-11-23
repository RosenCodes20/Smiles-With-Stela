document.addEventListener('DOMContentLoaded', () => {
    let called = document.querySelectorAll("#called");

    for (span of called) {
        if (screen.width < 448) {
            span.id = "none";
        }

        console.log(span);
    }
})