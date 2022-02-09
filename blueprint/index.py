from xml.etree.ElementPath import prepare_parent
from flask import render_template, Blueprint
from conexao import start_connection_db, close_connection_db

index = Blueprint('index',__name__,static_folder='static',template_folder='templates')

@index.route('')
@index.route('/home')
def home():
    cursor, conexao = start_connection_db()
    cursor.execute(f'SELECT * FROM produto WHERE id_produto <= 3')
    promocao = cursor.fetchall()
    print(promocao)

    cursor.execute(f'SELECT * FROM produto WHERE id_produto >3 AND id_produto <=5')
    novidades = cursor.fetchall()
    print(novidades)

    cursor.execute(f'SELECT * FROM produto WHERE seccao_produto=%s',('mais vendidos',))
    mais_vendidos = cursor.fetchall()
    print(mais_vendidos)

    close_connection_db(cursor,conexao)
    return render_template('index.html', promocao=promocao, novidades=novidades,mais_vendidos=mais_vendidos, image_static_url='/static/img/')