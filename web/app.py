# -*- coding: utf8 -*-
from flask import Flask, render_template, request
import hashlib
app = Flask(__name__)
users = {}

@app.route("/")
def hello():
    return render_template("login.html")

@app.route("/name")
def name():
    return "HR"

@app.route("/login" , methods=['POST'])
def login():
    id = request.form['id']
    pw = request.form['pw']
    if id in users:
        if users[id] == hashlib.sha1(pw).hexdigest():
            return "login ok"
        else:
            return "login fail"
    else:
        return "login fail"

@app.route("/join" , methods=['GET', 'POST'])
def join():
    if request.method == 'POST':
        id = request.form['id']
        pw = request.form['pw']
        if id not in users:
            users[id] = hashlib.sha1(pw).hexdigest()
        else:
            return "duplicate!!"
        return "join ok"
    return render_template("join.html")
        #return "id: %s, pw: %s" % (id, pw)
    #return render_template("join.html")

@app.route("/add")
@app.route("/add/<int:num1>")
@app.route("/add/<int:num1>/<int:num2>")
def add(num1=None, num2=None):
    if num1 is None or num2 is None:
        return "/add/num1/num2"
    return str(num1 + num2)
@app.route("/sub/<int:num1>/<int:num2>")
def sub(num1, num2):
    return str(num1 - num2)
@app.route("/multi/<int:num1>/<int:num2>")
def multi(num1,num2):
    return str(num1 * num2)
@app.route("/div")
@app.route("/div/<int:num1>")
@app.route("/div/<int:num1>/<int:num2>")
def div(num1=None, num2=None):
    if num1 is None or num2 is None:
        return "/div/num1/num2"
    if num1 is 0 or num2 is 0:
        return "Error"
    #float 소수점을 받아드리겠다 (@app.route("/div/<float:num1>/<float:num2>"))
    #if num2 != 0.0:
        #return str(num1/ num2)
    #else:
        #return "error"
    #이러면 소수점 입력이 가능하고 0을 입력했을때 에러가 뜬다
    return str(num1 / num2)

