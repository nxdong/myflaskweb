from flask import Flask
from flask import request
from flask import make_response
#from flask.ext.script import Manager

app = Flask(__name__)
#manager = Manager(app)
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie</h1>')
    response.set_cookie('answer', "42")
    return response

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello,%s!</h1>' % name
@app.before_first_request
def before():
    return 'header'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=9527)
#    manager.run()