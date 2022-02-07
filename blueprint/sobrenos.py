from flask import render_template, Blueprint

sobrenos = Blueprint('sobrenos',__name__,static_folder='static',template_folder='templates')

@sobrenos.route('')
def testemunhos():
    return render_template('sobrenos.html')