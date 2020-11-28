function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


function configure(selector, callback) {
    const formButtons = document.querySelectorAll(selector)

    for (let each of formButtons) {
        callback(each)
    }
}


function addClasses(selector, classes) {
    configure(selector, it => {
        it.classList.add(...classes.split(' '))
    })
}


M.AutoInit();

configure('.unassigned', it => {
    it.addEventListener('mousedown', e => {
        M.toast({html: 'Ой, но это пока не готово!'})
    })
})
