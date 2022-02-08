function validar(e) {
    e.preventDefault()
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const pass1 = document.getElementById("pass1").value;
    const pass2 = document.getElementById("pass2").value;

    if (nome == "" || nome == null) {
        alert("Erro o nome está vazio");
    }

    if (pass1 !== pass2) {
        alert("Erro as palavra-passes são diferentes");
    }
}

var btncadastrar = document.getElementById("btn-login");

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