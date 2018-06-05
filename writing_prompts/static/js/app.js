$(document).ready(function () {

    $('.tabs').tabs();

    // Switch board
    $("input").change(function () {
        if ($(this).is(":checked")) {
            console.log("Is checked");
            userName = $(this).data("username")
            document.location.href = document.URL + '/entries';
            $(this).css(':checked')
            // window.location = ;
        }
        else {
            console.log("Is Not checked");
        }
    })
})

$('#get-prompt').on('click', function () {
    $.get('https://ineedaprompt.com/dictionary/default/prompt?q=adj+noun+adv+verb+noun+location', function (prompt, status) {
        if (status === 'error') {
            console.log('something happend ');
        }
        else {
            console.log(prompt.english)
            $('#give-prompt').css('display', 'none')
            $('#give-prompt').html("<p>" + prompt.english + "</p>")
            $('#give-prompt').fadeIn(1000);
        }
    })
})
