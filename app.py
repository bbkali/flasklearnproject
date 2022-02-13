# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2022/02/13 19:47:14
@Author  :   bb 
@Desc    :   这是一个入门学习Flask的实战项目
'''

from flask import Flask, escape


app = Flask(__name__)


@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def user_page(name):
    # escape 可以转义html
    return 'hello %s!' % escape(name)
