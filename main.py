from flask import Flask, render_template

from flask import Flask

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria=categoria
        self.console=console

app = Flask(__name__)

@app.route('/inicio')
def ola():
    jogo1 = Jogo('Tetris', 'Puzzle', 'Ataria')
    jogo2 = Jogo('God of War', 'Rock n Slash', 'PS2')
    jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')

    lista = [jogo1, jogo2, jogo3]
    return render_template('listas.html', titulo='Jogos', jogos = lista)

app.run()
