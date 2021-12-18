function validar(e){

    e.preventDefault()
    const nome = document.getElementById("nome").value
    const password = document.getElementById("pass").value

    if(nome == null || nome=="")
    {
        alert("Erro: o nome não pode estar em branco")
    }

    if(password == null || password == "")
    {
        alert("Erro: a password está errada")
    }

    if(nome != null && nome != "")
    {
        if(password != null && password != "")
        {
            if(nome == "Creuma Kuzola" && password=="1234")
            {
                alert("Seja bem vinda: "+ nome)
            }
            else{
                alert("Erro: Este usuário não está cadastrado")
            }
        }
    }

}

var btnLogin = document.getElementById("btn-login")
btnLogin.addEventListener("click",validar)