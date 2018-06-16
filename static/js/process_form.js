function hideForm(yes) {
    if (yes) {
        $('#main-content').hide()
        $('#loading-content').show()
    } else {
        $('#main-content').show()
        $('#loading-content').hide()
    }
}

// Catch submission using the enter button
function enterKeySubmit(event) {
    console.log('Submission using enter key')
    if (event && event.keyCode == 13) {
        $('#main-form').submit()
    }
}

// Process form
$('#main-form').submit(function(event){
    hideForm(true)

    var that = $(this),
    url = '/process',
    method = that.attr('method'),
    data = {}

    // Find anything with the attribute of 'name'
    that.find('[name]').each(function(index, value) {
        var item = $(this),
        name = item.attr('name'),
        value = item.val()

        // Store it in the data object created above
        data[name] = value
    })

    console.log(data)

    // Submit data
    $.ajax({
        url: url,
        type: method,
        data: data,
        success: function(response) {
            console.log('Got a response from the server!')
            console.log(response)

            if (response['valid']) {
                $.redirect('/results', response['message'])
            } else {
                hideForm(false)
            }
        },
        error: function(response) {
            console.log('code should never run!')
        }
    })

    // Prevent HTML from submitting the form itself
    event.preventDefault()
})
