import random
import json

from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index/<title>')
def index(title):
    return render_template('base.html', title=title)


@app.route('/training/<prof>', methods=["GET"])
def training(prof):
    return render_template('training.html', profession=prof)


@app.route('/member')
def member():
    with open('templates/members.json', encoding='utf-8') as json_file:
        f = json_file.read()
        data = json.loads(f)
        number = random.randint(0, len(data) - 1)
        profs = sorted(data[number]["professions"])
    return render_template('member.html', index=number, json=data, professions=profs)


if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')
