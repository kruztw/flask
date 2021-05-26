# wsgi (Web Server Gateway Interface)
# client <--> NginX <--> WSGI <--> Flask
#
# 程式參考:  https://ithelp.ithome.com.tw/articles/10201217
# 架構參考: https://www.maxlist.xyz/2020/05/06/flask-wsgi-nginx/
from flask import Flask, render_template

class printMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, response_interface):
        """ environ: some information, includes client request info """
        #print(environ)
        #print(response_interface)
        print('— — — — — — — — — —')
        print('Function called')
        print('— — — — — — — — — —')
        return self.app(environ, response_interface)


app = Flask(__name__)
app.wsgi_app = printMiddleware(app.wsgi_app)


@app.route("/")
def home():
    return "hello_world"

app.run()
