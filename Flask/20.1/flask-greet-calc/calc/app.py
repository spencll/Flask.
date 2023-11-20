# Put your app in here.
from flask import Flask
app = Flask(__name__)

from operations import add,sub,mult,div
from flask import request

@app.route("/add")
def ab_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))

@app.route("/sub")
def ab_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route("/mult")
def ab_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route("/div")
def ab_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))

dict = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }
@app.route("/math/<action>")
def math(action):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(dict[action](a,b))
