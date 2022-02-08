from flask import render_template, Blueprint
from conexao import start_connection_db, close_connection_db

login = Blueprint('login',__name__,static_folder='static',template_folder='templates')

@login.route('')
def testemunhos():
    return render_template('login.html')

    