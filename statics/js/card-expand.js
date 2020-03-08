$(".expand-button").click(function() {
  $(this).closest('.recipe-box').animate({
    maxHeight: "100%"
}, 1000);

  $(this).remove();
});
