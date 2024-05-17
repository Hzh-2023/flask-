from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("book.html")

@app.route('/',methods = ['post'])
def loginpage():
    username = request.form['user']
    logyes="欢迎回来，"
    return render_template("book.html",username=username,logyes=logyes)

if __name__ == '__main__':
    app.run(port=61663,debug=True)
