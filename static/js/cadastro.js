function validar(e) {
    e.preventDefault()
    const nome = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const pass1 = document.getElementById("pass1").value;
    const pass2 = document.getElementById("pass2").value;

    if (nome == "" || nome == null) {
        alert("Erro o nome está vazio");
    }  
    
    if(pass1 !== pass2){
        alert("Erro as palavra-passes são diferentes");
    }
}

var btncadastrar = document.getElementById("btn-login");
btncadastrar.addEventListener("click", validar);
