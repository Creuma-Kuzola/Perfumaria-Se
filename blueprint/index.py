from flask import render_template, Blueprint

index = Blueprint('index',__name__,static_folder='static',template_folder='templates')

@index.route('')
def testemunhos():
    return render_template('index.html')