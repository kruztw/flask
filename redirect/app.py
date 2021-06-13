from flask import Flask, make_response, redirect, request

app = Flask(__name__)

@app.route("/redirect")
def set_cookie():
    resp = make_response(redirect("/"))
    return resp

@app.route("/")
def home():
    return "home"

app.run()
