# https://www.maxlist.xyz/2020/06/20/flask-uwsgi/
# https://www.maxlist.xyz/2020/06/17/flask-nginx-uwsgi-on-gcp/

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return 'run'

