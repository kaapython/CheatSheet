function on_check(event) {
    get_iss($(event).prop('checked'));
};

function get_iss(slice) {
    var csrftoken = $('input[name=csrfmiddlewaretoken]').val();

    $.ajax({
        url: 'get_iss',
        type: 'POST',
        data: {'slice': slice?'5':''},
        dataType: 'json',

        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);

        },

        success: function (response) {
            $('#place_works').html(response.html);
        },

        error: function (xhr, status, error) {
            console.log('error: ', error)
        }
    })
};