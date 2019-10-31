var Library = {};
$(function () {
    Library.Forms = {
        submitForm: function (elem) {
            var form = $(elem);
            var elemParent = form.parents('.form-container');
            var msgContainer = form.find('.alert');
            $.ajax({
                type: 'post',
                url: form.attr('action'),
                data: form.serialize()
            }).then(data => {
                console.log(data);
                if (data.app_status) {
                    if (data.status_code == 1) { // redirect
                        window.location = data.redirect_url
                    } else if (data.status_code == 2) { // show success message and stay on the current page
                        msgContainer.addClass('alert-success').removeClass('alert-danger').removeClass('hidden').html(data.message);
                        form[0].reset();
                    }
                } else {
                    msgContainer.addClass('alert-danger').removeClass('alert-success').removeClass('hidden').html(data.message);
                }
            });
        }
    }

});