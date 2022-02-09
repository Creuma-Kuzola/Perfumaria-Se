/*function formNewsletterValidation(e){
    e.preventDefalut()
    const nome = document.getElementById('nome')
    const email = document.getElementById('email')

    if (nome == "" || nome == null) {
        alert("Erro o nome está vazio");
    }

}

$('#btn-send').click(function(e) {
    formNewsletterValidation()
    alert('Entrei')
    $.ajax({
        url: 'http://localhost:5000/',
        type: 'post',
        dataType: 'json',
        data: $('#form-newsletter').serialize(),
        success: function(data) {
            window.location.pathname = '/'
        },
        complete: function() {
            window.location.pathname = '/'
        }
    });
});
*/