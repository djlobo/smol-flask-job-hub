```javascript
$(document).ready(function() {
    // Dashboard data retrieval
    $('#dashboard').on('load', function() {
        $.ajax({
            url: '/get_application_data',
            type: 'GET',
            success: function(response) {
                // Populate dashboard with response data
            },
            error: function(error) {
                console.log(error);
            }
        });
    });

    // New application form submission
    $('#new-application-form').on('submit', function(e) {
        e.preventDefault();
        let formData = new FormData(this);
        $.ajax({
            url: '/create_application',
            type: 'POST',
            data: formData,
            success: function(response) {
                // Handle success message
                alert('application-save-success');
            },
            error: function(error) {
                // Handle error message
                alert('application-save-error');
            }
        });
    });

    // Edit application form submission
    $('#edit-application-form').on('submit', function(e) {
        e.preventDefault();
        let formData = new FormData(this);
        $.ajax({
            url: '/edit_application',
            type: 'POST',
            data: formData,
            success: function(response) {
                // Handle success message
                alert('application-save-success');
            },
            error: function(error) {
                // Handle error message
                alert('application-save-error');
            }
        });
    });

    // File upload
    $('#file-upload').on('change', function() {
        let fileData = new FormData();
        fileData.append('file', this.files[0]);
        $.ajax({
            url: '/upload_file',
            type: 'POST',
            data: fileData,
            contentType: false,
            processData: false,
            success: function(response) {
                // Handle success message
                alert('file-upload-success');
            },
            error: function(error) {
                // Handle error message
                alert('file-upload-error');
            }
        });
    });

    // View application
    $('#view-application').on('click', function() {
        let applicationId = $(this).data('id');
        $.ajax({
            url: '/view_application/' + applicationId,
            type: 'GET',
            success: function(response) {
                // Populate view with response data
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
```