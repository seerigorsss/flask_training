from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>', methods=["GET"])
def training(prof):
    return render_template('training.html', profession=prof)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {}
    params['title'] = 'Анкета'
    params['surname'] = 'Watny'
    params['name'] = 'Mark'
    params['education'] = 'выше среднего'
    params['profession'] = 'штурман марсохода'
    params['sex'] = 'male'
    params['motivation'] = 'Всегда мечтал застрять на Марсе'
    params['ready'] = 'True'
    return render_template('auto_answer.html', values=params)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
