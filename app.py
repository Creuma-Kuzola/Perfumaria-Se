from flask import Flask, render_template, url_for

app = Flask(__name__ , template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/produtos')
def produtos():
    return render_template('produtos.html')   

@app.route('/testemunhosdosclientes')
def testemunhosdosclientes():
    return render_template('testemunhosdosclientes.html')

@app.route('/sobrenos')
def sobrenos():
    return render_template('sobrenos.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


if __name__ == "__main__":
    app.run(debug=True)