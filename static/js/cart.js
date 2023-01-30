document.addEventListener('DOMContentLoaded', () => {

    const pushmenu = document.getElementsByClassName('pushmenu');

    const hiddenOverley = document.querySelector('.hidden-overley1');

    const checkout = document.getElementsByClassName('btn-checkout');

    const hiddenOverley2 = document.querySelector('.cart-button');

    hiddenOverley2.addEventListener('click', (e) => {
        document.querySelector('.btn-checkout').classList.toggle('open');
        document.querySelector('.cart-button').classList.toggle('show');
        document.querySelector('.hidden-overley2').classList.toggle('show');
    });

    const checkoutFunction = function () {
        document.querySelector('.btn-checkout').classList.toggle('open');
        document.querySelector('.cart-button').classList.toggle('show');
        document.querySelector('.hidden-overley2').classList.toggle('show');

    };

    for (i = 0; i < checkout.length; i++) {
        checkout[i].addEventListener('click', checkoutFunction, false);
    }

    hiddenOverley.addEventListener('click', (e) => {
        e.currentTarget.classList.toggle('show');
        document.querySelector('.sidebar').classList.toggle('show');
        document.querySelector('body').classList.toggle('sidebar-opened');
        for (i = 0; i < pushmenu.length; i++) {
            pushmenu[i].classList.toggle('open');
        }
    });

    const pushmenuFunction = function () {
        document.querySelector('.pushmenu').classList.toggle('open');
        document.querySelector('.sidebar').classList.toggle('show');
        document.querySelector('.hidden-overley1').classList.toggle('show');
        document.body.classList.toggle('sidebar-opened')
    };

    for (i = 0; i < pushmenu.length; i++) {
        pushmenu[i].addEventListener('click', pushmenuFunction, false);
    }
});