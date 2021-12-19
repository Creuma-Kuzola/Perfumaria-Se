let menuVisible = true;


document.querySelector('.close-menu-button').addEventListener('click', () => {
  document.querySelector('.mobile-menu').style = 'display: none !important'
})


document.querySelector('.hamburguer-menu-icon').addEventListener('click', () => {
  document.querySelector('.mobile-menu').style = 'display: flex !important'
})