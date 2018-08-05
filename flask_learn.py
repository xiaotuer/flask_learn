from flask import Flask, request

app = Flask(__name__)  # type: Flask


@app.route('/')
def hello_world():
    return 'Hello World!'

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


if __name__ == '__main__':
    app.run()
