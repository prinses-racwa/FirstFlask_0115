from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil_pesan = None
    if request.method == "POST":
        nama_tamu = request.form.get("nama_tamu")
        pesan_tamu = request.form.get("pesan_tamu")
        hasil_pesan = f"Sugeng rawuh, {escape(nama_tamu)}! Pesanmu: '{escape(pesan_tamu)}' wis dicatet nang buku tamu."
    
    return render_template("index.html", hasil=hasil_pesan)

@app.route("/omah")
def hello():
    return "Hello, ges - (anggepen iki omahmu)"

@app.route("/teras")
def home():
    return "iki jenenge teras (halaman depan)"

@app.route("/ruang-tamu")
def about():
    return "iki jenenge ruang tamu (tentang isi rumah)"

@app.route("/tuan-rumah")
def profile():
    return "Hello, Rajwa! - iki jenenge sing ndue rumah"

@app.route("/nomoromah")
def post():
    return "Post #20 - iki jenenge nomor omahmu"

@app.route("/gambar-omah")
def gambar():
    return '<img src="https://p16-oec-sg.ibyteimg.com/tos-alisg-i-aphluv4xwc-sg/7e023184058340f688fc21e57513cc4f~tplv-aphluv4xwc-resize-jpeg:700:0.jpeg" />'

if __name__ == "__main__":
    app.run(debug=True)