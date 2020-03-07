$(document).ready(function() {
  $('.carousel').slick({

    centerMode: true,
    centerPadding: '360px',
    slidesToShow: 1,
    arrows: true,
    responsive: [{
        breakpoint: 1024,
        settings: {
          arrows: true,
          centerMode: true,
          centerPadding: '100px',
          slidesToShow: 1
        }
      },
      {
        breakpoint: 768,
        settings: {
          arrows: false,
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 1
        }
      }
    ]
  });
});
