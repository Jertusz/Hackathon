document.addEventListener("DOMContentLoaded", event => {
  document.getElementById("id_q").value = "";
});

document.getElementById("query").addEventListener(
  "keydown",
  function(e) {
    if (!e) {
      var e = window.event;
    }

    if (e.keyCode == 13) {
      var form_field = document.getElementById("query");
      var hidden_form_field = document.getElementById("id_q");

      if (form_field.value.length > 0) {
        hidden_form_field.value =
          hidden_form_field.value + " " + form_field.value;

        var $new_tag = $('<div class="tag">' + form_field.value + "</div>");

        $(".tags").append($new_tag);
        form_field.value = "";

        $(".tag").click(function() {
          var text = $("#id_q").val();
          text = text.replace($(this).text(), "");
          $("#id_q").val(text);

          $(this).remove();
        });
      }
    }
  },
  false
);
