from flask import render_template, Blueprint

produtos = Blueprint('produtos',__name__,static_folder='static',template_folder='templates')

@produtos.route('')
def testemunhos():
    return render_template('produtos.html')