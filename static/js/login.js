function validar(e) {

    e.preventDefault()
    const nome = document.getElementById("nome").value
    const password = document.getElementById("pass").value

    if (nome == null || nome == "") {
        alert("Erro: o nome não pode estar em branco")
    }

    if (password == null || password == "") {
        alert("Erro: a password está errada")
    }

}

var btnLogin = document.getElementById("btn-login")

$('#btn-login').click(function(e) {
    validar(e)
    $.ajax({
        url: 'http://localhost:5000/login',
        type: 'post',
        dataType: 'json',
        data: $('#form-login').serialize(),
        success: function(data) {
            window.location.pathname = '/'
        },
        complete: function() {
            window.location.pathname = '/'
        }
    });
});