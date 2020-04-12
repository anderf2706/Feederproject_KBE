$(document).ready(function() {
     $('form').on('submit', function(event) {
       $.ajax({
          data : {
             firstName : $('#firstName').val(),
             lastName: $('#lastName').val(),
                 },
             type : 'POST',
             url : '/process'
            })
        .done(function(data) {
          $('#output').text(data.output).show();
      });
      event.preventDefault();
      });
});