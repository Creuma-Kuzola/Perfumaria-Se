from flask import render_template, Blueprint, request
from conexao import start_connection_db, close_connection_db

login = Blueprint('login',__name__,static_folder='static',template_folder='templates')

@login.route('',methods=['GET','POST'])
def logins():
    print('Entrei asfdghjkl')
    if request.method == 'GET':
        return render_template('login.html')
    else:
        nome = request.form['nome']
        palavra_passe = request.form['pass']
        print('Dados login',nome,palavra_passe)
        cursor, conexao = start_connection_db()
        cursor.execute(f'SELECT nome_usuario, palavra_passe FROM usuario WHERE nome_usuario = %s and palavra_passe =%s',(nome,palavra_passe))
        usuario = cursor.fetchone()
        close_connection_db(cursor,conexao)

        if usuario != None:
            return render_template('index.html')
        return "<h1>Bla bla bla</h1>"    
       
        


        

