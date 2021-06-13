from flask import Flask, make_response, redirect, request, Response

app = Flask(__name__)

@app.route("/set")
def set_cookie():
    resp = make_response(redirect("/"))
    resp.set_cookie("key", "value")
    return resp

@app.route("/get")
def get_cookie():
    return request.cookies.get("key")

@app.route("/del")
def del_cookie():
    res = Response('delete cookie')
    res.set_cookie("key", "", expires=0)
    return res

@app.route("/")
def home():
    return "home"

app.run()
