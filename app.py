from flask import Flask, request
from markupsafe import escape
app = Flask(__name__)
@app.route("/omah")
def hello():
    return "Hello, ges" " -(anggepen iki omahmu)"

@app.route("/teras")
def home():
    return "iki jenenge teras (halaman depan)"

@app.route("/ruang tamu")
def about():
    return "iki jenenge ruang tamu (tentang isi rumah)"

@app.route("/tuan rumah")
def profile():
    return f"Hello, Rajwa!" " - iki jenenge sing ndue rumah"

@app.route("/nomoromah")
def post():
    return f"Post #20" "- iki jenenge nomor omahmu"

@app.route("/gambar omah")
def gambar():
    return f"</p> <img  src=https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/7e023184058340f688fc21e57513cc4f~tplv-aphluv4xwc-resize-jpeg:700:0.jpeg />"
