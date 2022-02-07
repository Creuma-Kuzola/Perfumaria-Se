from flask import Flask, render_template, url_for, request
from blueprint.testemunhosdosclientes import testemunhosdosclientes as testemunhosdosclientesBlueprint
from blueprint.index import index as indexBlueprint
from blueprint.produtos import produtos as produtosBlueprint
from blueprint.sobrenos import sobrenos as sobrenosBlueprint
from blueprint.login import login as loginBlueprint
from blueprint.cadastro import cadastro as cadastroBlueprint

app = Flask(__name__ , template_folder='templates')
app.register_blueprint(testemunhosdosclientesBlueprint,url_prefix='/testemunhosdosclientes')
app.register_blueprint(indexBlueprint, url_prefix='/')
app.register_blueprint(indexBlueprint, url_prefix='/home')
app.register_blueprint(produtosBlueprint, url_prefix='/produtos')
app.register_blueprint(sobrenosBlueprint, url_prefix='/sobrenos')
app.register_blueprint(loginBlueprint, url_prefix='/login')
app.register_blueprint(cadastroBlueprint, url_prefix='/cadastro')

if __name__ == "__main__":
    app.run(debug=True)