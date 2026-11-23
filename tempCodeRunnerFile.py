from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/")
def home():
    return "Home page"

@app.route("/about")
def about():
    return "About us"

@app.route("/user/<name>")
def profile(name):
    return f"Hello, {name}!"

@app.route("/post/<int:post_id>")
def post(post_id):
    return f"Post #{post_id}"