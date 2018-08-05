# -*- encoding:utf-8 -*-
from models import User
from flask import Flask, request, url_for, render_template
app = Flask(__name__)  # type: Flask
@app.route('/')
def hello_world():
    content = "小鸟唧唧jijij"
    return render_template("index.html", content=content)


@app.route('/user')
def user_index():
    user = User(1, 'baba ')
    return render_template('user_index.html', user=user)


if __name__ == '__main__':
    app.run()

