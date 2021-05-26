from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/nopage")
def nopage():
    return "Hello world!";


app.run()
