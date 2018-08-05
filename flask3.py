# -*- encoding:utf-8 -*-
from flask import Flask, render_template, flash,request
from wtforms import Form, TextField, PasswordField, validators, StringField
app = Flask(__name__) # type: Flask
app.secret_key = '123'


class LoginForm(Form):
    username = StringField("username", [validators.DataRequired()])
    password = PasswordField("username", [validators.DataRequired()])

@app.route('/')
def hello_world():
    myForm = LoginForm(request.form)
    flash("hello 小袅袅")
    return render_template("login.html", form=myForm)


@app.route('/login', methods=['POST'])
def login():
    myForm = LoginForm(request.form)
    form = request.form
    username = form.get('username')
    password = form.get('password')
    if not username:
        flash("please input username")
        return render_template("login.html", form=myForm)
    if not password:
        flash("please input password")
        return render_template("login.html", form=myForm)
    if myForm.username.data=="123" and myForm.password.data == "321" and myForm.validate():
        flash("login success")
        return render_template("login.html", form=myForm)
    else:
        flash("username or password is wrong")
        return render_template("login.html", form=myForm)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")


@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id) == 1:
        return render_template("user.html")
    else:
        return  render_template("404.html")



if __name__ == '__main__':
    app.run()