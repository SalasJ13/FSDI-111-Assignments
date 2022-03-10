from flask import Flask

app = Flask(__name__)


@app.route("/")
def about_me():
    me = {
        "first_name": "Jazmin",
        "last_name": "Salas",
        "hobbies": "Read",
        "active": True
    }
    return me


@app.route("/greet/<fname>/<lname>/")
def greet_user(fname, name):
    return "<h1>Hello word, %s</h1>" % (name, fname)


@app.route("/square/<int:num/>")
def square_num(num):
    return "<h1>%s squared is: %s</h1>" % (num, num*num)
