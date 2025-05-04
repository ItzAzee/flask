from flask import Flask, render_template

app = Flask(__name__)

params = {'title': 'title', 'surname': 'surname', 'name': 'name', 'education': 'education', 'sex': 'sex',
          'motivation': 'motivation', 'profession': 'profession', 'ready': 'ready'}


@app.route('/<word>')
@app.route('/index/<word>')
def index(word):
    return render_template('base.html', title=word)


@app.route('/answer')
def answer():
    return render_template('auto_answer.html', **params)


@app.route('/auto_answer')
def auto_answer():
    return render_template('auto_answer.html', **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
