from flask import render_template, Blueprint

testemunhosdosclientes = Blueprint('testemunhosdosclientes',__name__,static_folder='static',template_folder='templates')

@testemunhosdosclientes.route('')
def testemunhos():
    return render_template('testemunhosdosclientes.html')