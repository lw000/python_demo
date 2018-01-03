#!/usr/bin/env python
# -*- coding=utf-8 -*-

'''
Created on 2018年1月3日

@author: Administrator
'''

from flask import Flask
from flask import request
from flask import render_template

# from flask import sessions

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
#     return '<h1>Home</h1>'
    return render_template('./home.html')

@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
              <p><input name="username"></p>
              <p><input name="password" type="password"></p>
              <p><button type="submit">Sign In</button></p>
              </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    # 需要从request对象读取表单内容：
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


@app.route('/add', methods=['GET'])
def add():
#     v = sessions[""]

    print(request.args.items().__str__())
    
    a = request.args.get('a')
    b = request.args.get('b')
    
#     if not isinstance(a, int):
#         raise ValueError('a must be an integer!')
#     if not isinstance(b, int):
#         raise ValueError('b must be an integer!')
    
    return str(int(a) + int(b))


@app.route('/sub', methods=['GET'])
def sub():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) - int(b))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
