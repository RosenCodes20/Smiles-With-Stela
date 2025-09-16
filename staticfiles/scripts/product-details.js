document.addEventListener('DOMContentLoaded', () => {
    const mainImage = document.getElementById("main-image");
    const thumbnails = document.querySelectorAll(".gallery img");
    
    thumbnails.forEach(img => {
        img.addEventListener("click", () => {
            mainImage.src = img.src;
        });
    });
})
