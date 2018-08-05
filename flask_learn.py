from flask import Flask

app = Flask(__name__)  # type: Flask


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user', methods=['POST'])
def hello_user():
    return 'Hello User!'


if __name__ == '__main__':
    app.run()
