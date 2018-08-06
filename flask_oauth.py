# -*- encoding:utf-8 -*-
import base64
import random

import time
from flask import Flask, request

app = Flask(__name__) # type: Flask

users = {
    "miko" : ["123456"]
}
def gen_token(uid):
    str2 = ':'.join([str(uid), str(random.random()), str(time.time() + 7200)]).encode()
    # print(str2.decode())
    token = base64.b64encode(str2)

    users[uid].append(token.decode())
    return token

def verify_token(token):
    print('token: ', token)
    _token = base64.b64decode(token.encode()).decode()
    print('_token: ',_token)
    # 对比token
    if not users.get(_token.split(':')[0])[-1] == token:
        print(users)
        return -1
    # 是否超时
    if float(_token.split(":")[-1]) >= time.time():
        return 1
    else:
        return 0


@app.route('/index', methods=['POST', 'GET'])
def index():
    print(request.headers)
    return 'hello'


@app.route('/login', methods=['POST', 'GET'])
def login():
    str1 = str(request.headers['Authorization'].split(' ')[-1]).encode()
    uid, pw = (base64.b64decode(str1)).decode().split(':')
    print(uid)
    if users.get(uid)[0] == pw:
        return gen_token(uid)
    else:
        return 'error'

@app.route('/test', methods=['POST', 'GET'])
def test():
    token = request.args.get('token')
    print(verify_token(token))
    if verify_token(token) == 1:
        return 'data'
    else:
        return 'error'




if __name__ == '__main__':
    app.run()