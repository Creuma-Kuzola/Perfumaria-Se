import re
from flask import render_template, Blueprint, request
from conexao import start_connection_db, close_connection_db

produtos_compra = Blueprint('produtos_compra',__name__,static_folder='static',template_folder='templates')

@produtos_compra.route('/<int:produto_id>')
def produto(produto_id):
   if request.method == 'GET':
    cursor, conexao = start_connection_db()
    cursor.execute(f'SELECT * FROM produto WHERE id_produto=%s',(produto_id,))
    produto = cursor.fetchone()
    close_connection_db(cursor,conexao)
    print(produto_id)
    print(produto)
    return render_template('produtocompra.html',produto=produto,image_static_url='/static/img/')
   #else:
       