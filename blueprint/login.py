from flask import render_template, Blueprint

login = Blueprint('login',__name__,static_folder='static',template_folder='templates')

@login.route('')
def testemunhos():
    return render_template('login.html')