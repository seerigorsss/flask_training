from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>', methods=["GET"])
def training(prof):
    return render_template('training.html', profession=prof)


@app.route('/table/<sex>/<age>')
def table(sex, age):
    return render_template('table.html', sex=sex, age=int(age))


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
