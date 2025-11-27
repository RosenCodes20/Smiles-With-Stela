document.addEventListener('DOMContentLoaded', () => {
    let spans = document.querySelectorAll('.called');
    spans.forEach(span => {
        if (window.innerWidth < 808) {
            span.style.display = 'none';
        }
    });
})