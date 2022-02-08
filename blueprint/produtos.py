from flask import render_template, Blueprint
from conexao import start_connection_db, close_connection_db

produtos = Blueprint('produtos',__name__,static_folder='static',template_folder='templates')

@produtos.route('')
def produto():
    cursor, conexao = start_connection_db()

    cursor.execute(f'SELECT * FROM produto WHERE seccao_produto=%s',('promocao',))
    promocao = cursor.fetchall()

    cursor.execute(f'SELECT * FROM produto WHERE seccao_produto=%s',('novidades',))
    novidades = cursor.fetchall()

    cursor.execute(f'SELECT * FROM produto WHERE seccao_produto=%s',('mais vendidos',))
    mais_vendidos = cursor.fetchall()

    cursor.execute(f'SELECT * FROM produto WHERE seccao_produto=%s',('produtos',))
    produto1 = cursor.fetchall()

    close_connection_db(cursor,conexao)
    return render_template('produtos.html',promocao=promocao,novidades=novidades,mais_vendidos=mais_vendidos,produto1=produto1,image_static_url='/static/img/')