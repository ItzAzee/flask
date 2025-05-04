from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<word>')
@app.route('/index/<word>')
def index(word):
    return render_template('base.html', title=word)


@app.route('/distribution')
def distribution():
    p = ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', astronauts=p)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
