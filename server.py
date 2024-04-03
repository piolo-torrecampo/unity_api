from flask import Flask
import json

app = Flask(__name__)

@app.route("/rotate")
def rotate():
    file = open (r"data\rotate.json", "r")
    data = json.loads(file.read())
    return data

@app.route("/scale")
def scale():
    file = open (r"data\scale.json", "r")
    data = json.loads(file.read())
    return data

@app.route("/remove")
def remove():
    file = open (r"data\remove.json", "r")
    data = json.loads(file.read())
    return data

@app.route("/replace")
def replace():
    file = open (r"data\replace.json", "r")
    data = json.loads(file.read())
    return data

@app.route("/move")
def move():
    file = open (r"data\move.json", "r")
    data = json.loads(file.read())
    return data

@app.route("/insert")
def insert():
    file = open (r"data\insert.json", "r")
    data = json.loads(file.read())
    return data