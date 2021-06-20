from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def home():
    resp = Response("redirect to google in 2 seconds")
    resp.headers['Refresh'] = "2; url=http://google.com"
    return resp

app.run()
