// static/js/admin.js
(function ($) {
  $(document).ready(function () {
    $('#id_merek').change(function () {
      var url = window.location.origin + '/aplikasi/jenis_ajax/';
      var merekId = $(this).val();
      $.ajax({
        url: url,
        data: {
          merek: merekId,
        },
        success: function (data) {
          var $jenis = $('#id_jenis');
          $jenis.find('option').remove();
          $.each(data, function (index, item) {
            $jenis.append(
              $('<option></option>').attr('value', item.id).text(item.name)
            );
          });
        },
      });
    });
  });
})(django.jQuery);
