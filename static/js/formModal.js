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
                formModal.querySelector('.modal-title').textContent = 'Update a ' + data.name + ' recipe.'
                $('#recipe-name').val(data.name);
                $('#recipe-time').val(data.time);
                $('#recipe-water').val(data.water);
                $('#recipe-coffee').val(data.coffee);
                $('#recipe-description').val(data.description);
            }
        });
    }
    else {
        formModal.querySelector('.btn-primary').textContent = "Create"
        formModal.querySelector('.modal-title').textContent = 'Create a new recipe.'
        $('#recipe-name').val('');
        $('#recipe-time').val('');
        $('#recipe-water').val('');
        $('#recipe-coffee').val('');
        $('#recipe-description').val('');
        document.getElementById('recipe-form').setAttribute('action', "/")
    }
})

var deleteModal = document.getElementById('deleteModal')
deleteModal.addEventListener('show.bs.modal', function (event) {
    var buttonDelete = event.relatedTarget
    var recipeDelete = buttonDelete.getAttribute('data-recipe-delete-id')
    if (recipeDelete != null) {
        document.getElementById('recipe-delete').setAttribute('action', "/delete/" + recipeDelete)
    }
})