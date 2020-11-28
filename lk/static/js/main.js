// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.carousel');
//     var instances = M.Carousel.init(elems, {
//         fullWidth: true,
//         indicators: true,
//         padding: 100
//     });
// });


$('.carousel.carousel-slider').carousel({
    fullWidth: true,
    indicators: true,
    padding: 100
});

function autoplay() {
    $('.carousel').carousel('next');
    setTimeout(autoplay, 4500);
}

autoplay();


show.visible = '2';
show.hidden = '3';

function show(){
    show.hidden = show.visible;
    show.visible = (show.visible === '2')?'3':'2';
    document.getElementById(show.visible).style.display = 'block';
    document.getElementById(show.hidden).style.display = 'none';
}


var error_response = function(data){
    //$('.api-response').html("API Response: " + data.status + ' ' + data.statusText + '<br/>Content: ' + data.responseText);
    // let a = data.responseText;
    let a = data[Object.keys(data)[18]]
    let b = JSON.stringify(a).split(separator=':')[1].split(separator='"')[1].split(separator="\\")[0];
    $('.api-response').html(b);
}

var susccess_response = function(data){
    // $('.api-response').html("API Response: OK<br/>Content: " + JSON.stringify(data));
    // var delayInMilliseconds = 100; //1 second
    // setTimeout(function() {
        window.location.reload()
        //your code to be executed after 1 second
    // }, delayInMilliseconds);
}

$().ready(function(){
    $('form.ajax-post button[type=submit]').click(function(){
        var form = $('form.ajax-post');
        $.post(form.attr('action'), form.serialize())
            .fail(function(data){error_response(data);})
            .done(function(data){susccess_response(data);});
        return false;
    });
});
