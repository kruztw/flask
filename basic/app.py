from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/<path:path>")
def others(path):
    arg1 = request.args.get('arg1')
    res = jsonify({'err': f'Page {path} not found', 'arg1': arg1})
    res.status_code = 404
    return res

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/nopage")
def nopage():
    return "Hello world!"


@app.route("/", methods=["post"])
def POST():
    # request.form.get('xxx')
    return "POST"

app.run()
