from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/<path:path>")
def others(path):
    arg1 = request.args.get('arg1')
    res = jsonify({'err': f'Page {path} not found', 'arg1': arg1})
    res.status_code = 404
    return res

@app.before_first_request
def before1():
    print("before1")
    return None

@app.before_request
def before2():
    print("before2")
    return None

@app.before_request
def before2():
    print("before3")
    return None

@app.route('/')
def home():
    print("home")
    return "home"

@app.after_request
def after1(resp):
    print("after1")
    return resp

@app.after_request
def after2(resp):
    print("after2")
    return resp

app.run()
