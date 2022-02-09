from flask import render_template, Blueprint, request
from conexao import start_connection_db, close_connection_db

index = Blueprint('index',__name__,static_folder='static',template_folder='templates')

@index.route('',methods=['GET','POST'])
@index.route('/home', methods=['GET','POST'])
def home():
    cursor, conexao = start_connection_db()
    cursor.execute(f'SELECT * FROM produto WHERE id_produto <= 3')
    promocao = cursor.fetchall()

    cursor.execute(f'SELECT * FROM produto WHERE id_produto >3 AND id_produto <=5')
    novidades = cursor.fetchall()
  
    cursor.execute(f'SELECT * FROM produto WHERE seccao_produto=%s',('mais vendidos',))
    mais_vendidos = cursor.fetchall()

    cursor.execute(f'SELECT * FROM testemunho WHERE id_testemunho <= 3')
    testemunho = cursor.fetchall()

    close_connection_db(cursor,conexao)
    
    if request.method == 'GET':
        return render_template('index.html', promocao=promocao, novidades=novidades,mais_vendidos=mais_vendidos, image_static_url='/static/img/',testemunho=testemunho)
    else:
        nome = request.form['nome']
        email = request.form['email']
        print(nome,email)
        cursor, conexao = start_connection_db()
        cursor.execute(f'INSERT INTO newsletter (nome,email) values (%s,%s)',(nome,email))
        conexao.commit()
        close_connection_db(cursor,conexao) 
        return render_template('index.html', promocao=promocao, novidades=novidades,mais_vendidos=mais_vendidos, image_static_url='/static/img/',testemunho=testemunho)

@index.route('/get/testemunho', methods=['GET','POST'])
def test():
    cursor, conexao = start_connection_db()
    cursor.execute(f'SELECT * FROM testemunho WHERE id_testemunho <= 3')
    testemunho = cursor.fetchall()
    close_connection_db(cursor,conexao)
    return {'result': testemunho}