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
            promptObj = {}
            promptObj.noun1 = prompt.components[0].english
            promptObj.verb1 = prompt.components[1].words[0].text
            promptObj.verb2 = prompt.components[1].words[1].text
            promptObj.noun2 = prompt.components[2].english
            promptObj.location = prompt.components[3].english
            renderPrompt(promptObj, prompt.english)
            // $('#give-prompt').css('display', 'none')
            // $('#give-prompt').html("<p>" + prompt.english + "</p>")
            // $('#give-prompt').fadeIn(1000);
        }
    })
})

function renderPrompt(data, prompt) {
    console.log(prompt)
    $("#ajax-prompt").val(prompt);
    console.log($('#ajax-prompt').val())
    style = {
        'display': 'none',
        'text-decoration': 'underline'
    }
    // for (let key in data) {
    //     $('#' + data[key] +'').css('display', 'none')
    //     $('#' + data[key] +'').html(data[key]).fadeIn(1000)
    // }
    $('#noun1').css(style)
    $('#noun1').html(data.noun1).fadeIn(Math.floor(Math.random() * 5000) + 500)
    $('#verb1').css('display', 'none')
    $('#verb1').html(data.verb1).fadeIn(Math.floor(Math.random() * 5000) + 500)
    $('#verb2').css('display', 'none')
    $('#verb2').html(data.verb2).fadeIn(Math.floor(Math.random() * 5000) + 500)
    $('#noun2').css('display', 'none')
    $('#noun2').html(data.noun2).fadeIn(Math.floor(Math.random() * 5000) + 500)
    $('#location').css('display', 'none')
    $('#location').html(data.location).fadeIn(Math.floor(Math.random() * 5000) + 500)
}