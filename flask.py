# Put your app in here.
from flask import Flask, request
from operations import add, subtract, mult, div

app = Flask(__name__)


@app.route('/add')
def do_add(a, b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)


@app.route('/sub')
def add(a, b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)


@app.route('/mult')
def add(a, b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)


@app.route('/div')
def add(a, b):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return str(result)
