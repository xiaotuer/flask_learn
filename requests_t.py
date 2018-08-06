# -*- encoding:utf-8 -*-
import requests

# r = requests.get('http://127.0.0.1:5000/login', auth=('miko', '123456'))
# print(r.text)


# 请求数据部分
token = 'bWlrbzowLjk5MDg5ODg2OTQ2NjIwODoxNTMzNTUyMDUyLjcwMDIxMQ=='
r = requests.get('http://127.0.0.1:5000/test', params={'token': token})
print(r.text)