var formModal = document.getElementById('formModal')
formModal.addEventListener('show.bs.modal', function (event) {
    var button = event.relatedTarget
    var recipe = button.getAttribute('data-recipe-id')
    if (recipe != null) {
        formModal.querySelector('.btn-primary').textContent = "Update"
        document.getElementById('recipe-form').setAttribute('action', "/update/" + recipe)
        $.ajax({
            url: "/update/" + recipe,
            method: "GET",
            success: function (data) {
                var modal = $(this)
                formModal.querySelector('.modal-title').textContent = 'Update a ' + recipe + ' recipe.'
                $('#recipe-name').val(data.name);
                $('#recipe-time').val(data.time);
                $('#recipe-water').val(data.water);
                $('#recipe-coffee').val(data.coffee);
                $('#recipe-description').val(data.description);
            }
        });
    }
    else {
        document.getElementById('recipe-form').setAttribute('action', "/")
        formModal.querySelector('.btn-primary').textContent = "Create"
        formModal.querySelector('.modal-title').textContent = 'Create a new recipe.'
    }
})