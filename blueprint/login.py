from flask import render_template, Blueprint, request
from conexao import start_connection_db, close_connection_db

login = Blueprint('login',__name__,static_folder='static',template_folder='templates')

@login.route('')
def testemunhos():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        nome = request.form['nome']
        pass1 = request.form['pass1']

        print('Dados login',nome,pass1)

