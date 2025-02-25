let menu = document.querySelector('.menu');
let section = document.querySelector('.section-info');

menu.addEventListener('click', () => {
    section.classList.toggle('menu-active');
});
