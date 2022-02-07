from flask import render_template, Blueprint

cadastro = Blueprint('cadastro',__name__,static_folder='static',template_folder='templates')

@cadastro.route('')
def testemunhos():
    return render_template('cadastro.html')