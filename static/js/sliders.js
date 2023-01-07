window.onload = function () {
    let image_slider = new Swiper('.image-slider', {
        loop: true,
        pagination: {
            el: '.swiper-pagination',
            clickable: true
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        }
    });

    let recomend = new Swiper('.recomend-slider', {
        slidesPerView: 4,
        spaceBetween: 23,
        centeredSlides: true,
        loop: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        }
    });

    let popular = new Swiper('.popular-slider', {
        slidesPerView: 4,
        spaceBetween: 23,
        centeredSlides: true,
        loop: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        }
    });
};