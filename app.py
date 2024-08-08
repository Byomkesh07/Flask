from flask import Flask

## WSGI (Web Server Gateway Interface) Application

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to my first web application"

@app.route('/members')
def members():
    return "Welcome to my first web applications member page"

if __name__ == '__main__':
    app.run(debug=True)
