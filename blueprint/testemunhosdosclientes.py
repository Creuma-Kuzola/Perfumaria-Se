from flask import render_template, Blueprint,request
from conexao import start_connection_db, close_connection_db

testemunhos_dos_clientes = Blueprint('testemunhos_dos_clientes',__name__,static_folder='static',template_folder='templates')

@testemunhos_dos_clientes.route('',methods=['GET','POST'])
def testemunhos():
    return render_template('testemunhosdosclientes.html')

@testemunhos_dos_clientes.route('/get/testemunho', methods=['GET','POST'])
def rota():
    cursor, conexao = start_connection_db()
    cursor.execute(f'SELECT * FROM testemunho LIMIT 3')
    testemunho = cursor.fetchall()
    close_connection_db(cursor,conexao)
    return {'result': testemunho}

@testemunhos_dos_clientes.route('/get/testemunhos', methods=['GET','POST'])
def test():
    cursor, conexao = start_connection_db()
    cursor.execute(f'SELECT * FROM testemunho')
    testemunho = cursor.fetchall()
    close_connection_db(cursor,conexao)
    return {'result': testemunho}