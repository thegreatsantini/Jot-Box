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