from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome=nome
        self.categoria=categoria
        self.console=console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('god of War', 'Rack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)

"""------------------------- Página Inicial ------------------------- """

@app.route('/')
def index():
    return render_template('lista.html', titulo='Jogos', jogos=lista)

"""------------------------- Página Add Jogo ------------------------- """

@app.route('/novo')
def novo():
    return render_template('novoJogo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect('/')


app.run(debug=True)