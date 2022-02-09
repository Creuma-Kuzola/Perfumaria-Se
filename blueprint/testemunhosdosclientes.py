from crypt import methods
from flask import render_template, Blueprint,request

testemunhos_dos_clientes = Blueprint('testemunhos_dos_clientes',__name__,static_folder='static',template_folder='templates')

@testemunhos_dos_clientes.route('',methods=['GET','POST'])
def testemunhos():
    return render_template('testemunhosdosclientes.html')