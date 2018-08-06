# -*- encoding:utf-8 -*-
from random import random

from models import User
from flask import Flask, request, url_for, render_template, redirect
app = Flask(__name__)  # type: Flask
auth_code = {}

@app.route('/')
def hello_world():
    content = "小鸟唧唧jijij"
    return render_template("index.html", content=content)


@app.route('/user')
def user_index():
    user = User(1, 'baba ')
    return render_template('user_index.html', user=user)


@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, '小鸟儿')

    return render_template('user_id.html', user=user)


@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, '小鸟儿'+str(i))
        users.append(user)
    return render_template("user_list.html", users=users)


@app.route("/one")
def one_base():
    return render_template("one_base.html")


@app.route("/two")
def two_base():
    return render_template("two_base.html")


@app.route("/client/login", methods=['POST', 'GET'])
def client_login():
    url = 'http://localhost:5000/oauth'
    return redirect(url)


@app.route("/oauth", methods=['POST', 'GET'])
def oauth():
    if request.args.get('code'):
        if auth_code.get(int(request.args.get('code'))) == request.args.get('redirect_url'):
            return gen_code(request.args.get('client_id'))
    return 'Please login...'


def gen_code(url):
    code = random.randint(0, 10000)
    auth_code[code] = url






if __name__ == '__main__':
    app.run()

