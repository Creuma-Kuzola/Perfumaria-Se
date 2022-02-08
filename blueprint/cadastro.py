from crypt import methods
from lib2to3.pgen2.token import EQUAL
from flask import render_template, Blueprint, request
from conexao import start_connection_db, close_connection_db

cadastro = Blueprint('cadastro',__name__,static_folder='static',template_folder='templates')

@cadastro.route('', methods=['GET','POST'])
def cadastrar():
    print(request.method)
    if request.method == 'GET':
        return render_template('cadastro.html')
    else:
         nome = request.form['nome']
         email = request.form['email']
         pass1 = request.form['pass1']
         print('Dados',nome,email,pass1)
         
         cursor, conexao = start_connection_db()
         cursor.execute(f'INSERT INTO usuario(nome_usuario,email,palavra_passe) VALUES(%s, %s, %s)', (nome,email,pass1))
         conexao.commit()
         close_connection_db(cursor,conexao)
         return render_template('login.html')