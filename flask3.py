# -*- encoding:utf-8 -*-
from flask import Flask, render_template, flash,request

app = Flask(__name__) # type: Flask
app.secret_key = '123'

@app.route('/')
def hello_world():
    flash("hello 小袅袅")
    return render_template("login.html")


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash("please input username")
        return render_template("login.html")
    if not password:
        flash("please input password")
        return render_template("login.html")
    if username=="123" and password == "321":
        flash("login success")
        return render_template("login.html")
    else:
        flash("username or password is wrong")
        return render_template("login.html")





if __name__ == '__main__':
    app.run()