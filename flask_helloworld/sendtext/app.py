#coding:utf-8

from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',title="helloworld")


@app.route('/sendtext', methods=['POST'])
def sendtext():
    return render_template('index.html',title=request.form['message'])

app.run()