document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('search-bar').style.display = 'none';

    document.getElementById('search-icon').addEventListener('click', function () {
        let searchBar = document.getElementById('search-bar');

        if (searchBar.style.display === 'none' || searchBar.style.display === '') {
            searchBar.style.display = 'block';
        } else {
            searchBar.style.display = 'none';
        }
    });

    document.querySelector(".item-items > .registration > ul > #search-icon").addEventListener("click", function () {
        let searchBar = document.querySelector('.item-items > .registration > ul > section');

        if (searchBar.style.display === 'none' || searchBar.style.display === '') {
            searchBar.style.display = 'block';
        } else {
            searchBar.style.display = 'none';
        }
    })
})