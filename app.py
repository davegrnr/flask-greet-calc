# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def run_add():
    """adds a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = add(a, b)

    return str(res)

@app.route('/sub')
def run_sub():
    """subtracts b from a"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = sub(a, b)

    return str(res)

@app.route('/mult')
def run_mult():
    """multiplies a and b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = mult(a, b)

    return str(res)

@app.route('/div')
def run_div():
    """divides a by b"""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = div(a, b)

    return str(res)

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do arithmetic for parameters."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)