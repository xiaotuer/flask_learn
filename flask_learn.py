from flask import Flask, request, url_for, render_template
from models import User
app = Flask(__name__)  # type: Flask


@app.route('/')
def hello_world():
    content = "小鸟唧唧jijij"
    return render_template("index.html", content=content)

# 指定方式
@app.route('/user', methods=['POST'])
def hello_user():
    return 'Hello User!'

# 传递参数
@app.route('/users/<id>')
def user_id(id):
    return 'hello: user ' + id

@app.route('/query_user')
def query_user():
    id = request.args.get('id')
    return 'query user: ' + id


# 反向路由
@app.route('/query_url')
def query_url():
    return 'query_url: ' + url_for('query_user')

if __name__ == '__main__':
    app.run()
