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

    if (nome != null && nome != "") {
        if (password != null && password != "") {
            if (nome == "Creuma Kuzola" && password == "1234") {
                alert("Seja bem vinda: " + nome)
            } else {
                alert("Erro: Este usuário não está cadastrado")
            }
        }
    }

}

var btnLogin = document.getElementById("btn-login")

$('#btn-login').click(function(e) {
    validar(e)
    $.ajax({
        url: 'http://localhost:5000/cadastro',
        type: 'post',
        dataType: 'json',
        data: $('#form-cadastro').serialize(),
        success: function(data) {
            window.location.pathname = '/login'
        },
        complete: function() {
            window.location.pathname = '/login'
        }
    });
});