const button = document.querySelector('.navigation__button--js')
button.addEventListener( 'click', () => {
    const nav = document.querySelector(".navigation--js");
    nav.classList.toggle('navigation--open');
})

const buttom = document.querySelector('.navigation__button--js')
buttom.addEventListener( 'click', () => {
    const nav = document.querySelector(".bar__zero--js");
    nav.classList.toggle('line__zero--js');
})

/*krzyżyk*/

const buttons = document.querySelector('.navigation__button--js')
buttons.addEventListener( 'click', () => {
    const nav = document.querySelector(".bar__first--js");
    nav.classList.toggle('line__first--js');
    
})

const buttonik = document.querySelector('.navigation__button--js')
buttonik.addEventListener( 'click', () => {
    const nav = document.querySelector(".bar__second--js");
    nav.classList.toggle('line__second--js');
})