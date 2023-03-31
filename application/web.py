
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 06:52:54 2021
app web
@author: chakib
"""

from flask import Flask, flash, redirect, render_template, request, session, abort

#configure the app
app = Flask(__name__)

#main page
@app.route("/")
def index():
    words = ["hello", "visitor", "thank", "you"]
    return render_template('index.html', title="welcome", words=words)
    
#contact page
@app.route('/contact')
def contact():
    mail = "john@doe.com"
    tel = "01 02 03 04 05"
    return "mail: "+mail+" --- phone: "+tel

#member page
@app.route("/members")
def members():
    name = "john doe"
    return name

#member name page
@app.route("/members/<string:name>/")
def getMember(name):
    return name

#run the app
app.run(host='172.17.0.2',port=5000)
# web.py
# Affichage de 23-web.py