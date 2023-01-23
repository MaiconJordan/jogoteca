from flask import Flask, render_template

from flask import Flask

app = Flask(__name__)

@app.route('/inicio')
def ola():
    return render_template('listas.html')

app.run()