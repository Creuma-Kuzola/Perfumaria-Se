
var btnEnviar = document.getElementById("btn-send");
btnEnviar.addEventListener("Click",validar)

function validar (e)
{
    e.preventDefault()
    const nome = document.getElementById("nome")
    const email = document.getElementById("email")
    if(nome == null || nome == "")
    {
        alert("Erro: O nome está em branco")
        nome.focus();
    }

    if(email == null || nome == ""){
        alert("Erro: o email está em branco")
        nome.focus();
    }
}