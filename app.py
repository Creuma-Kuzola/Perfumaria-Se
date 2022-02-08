from flask import Flask, render_template
from blueprint.testemunhosdosclientes import testemunhos_dos_clientes as testemunhosdosclientesBlueprint
from blueprint.index import index as indexBlueprint
from blueprint.produtos import produtos as produtosBlueprint
from blueprint.sobrenos import sobrenos as sobrenosBlueprint
from blueprint.login import login as loginBlueprint
from blueprint.cadastro import cadastro as cadastroBlueprint
from blueprint.produtoscompra import produtos_compra as produtosCompraBlueprint
from conexao import start_connection_db, close_connection_db

#cursor, conexao = start_connection_db()
#cursor.execute(f'INSERT INTO newsletter(nome, email) VALUES(%s, %s)', ('Creuma', 'cxxxx@gmail.com',))
#conexao.commit()
#close_connection_db(cursor,conexao)

app = Flask(__name__ , template_folder='templates')
app.register_blueprint(testemunhosdosclientesBlueprint,url_prefix='/testemunhosdosclientes')
app.register_blueprint(indexBlueprint, url_prefix='/')
app.register_blueprint(produtosBlueprint, url_prefix='/produtos')
app.register_blueprint(sobrenosBlueprint, url_prefix='/sobrenos')
app.register_blueprint(loginBlueprint, url_prefix='/login')
app.register_blueprint(cadastroBlueprint, url_prefix='/cadastro')
app.register_blueprint(produtosCompraBlueprint, url_prefix='/produto/compra')


if __name__ == "__main__":
    app.run(debug=True)