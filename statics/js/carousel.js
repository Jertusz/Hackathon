$(document).ready(function() {
  $('.carousel').slick({

    centerMode: true,
    centerPadding: '500px',
    slidesToShow: 1,
    arrows: false,
    infinite: false,
    responsive: [{
        breakpoint: 1600,
        settings: {
          centerMode: true,
          centerPadding: '350px',
          slidesToShow: 1
        }
      },
      {
        breakpoint: 1400,
        settings: {
          centerMode: true,
          centerPadding: '200px',
          slidesToShow: 1
        }
      },
      {
        breakpoint: 1024,
        settings: {
          centerMode: true,
          centerPadding: '100px',
          slidesToShow: 1
        }
      },
      {
        breakpoint: 768,
        settings: {
          centerMode: true,
          centerPadding: '40px',
          slidesToShow: 1
        }
      }
    ]
  });
});

$("#arrow-left").click(function() {
  $('.carousel').slick('slickPrev');
});

$("#arrow-right").click(function() {
  $('.carousel').slick('slickNext');
});
