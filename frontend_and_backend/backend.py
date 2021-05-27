from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/<path:path>")
def others(path):
    res = jsonify({'err': f'Page {path} not found'})
    res.status_code = 404
    return res

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/nopage")
def nopage():
    return "Hello world!"

app.run(host="127.0.0.1", port=3000)
