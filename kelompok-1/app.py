from flask import Flask, render_template, request
from models import hitung_kalori, rekomendasi_latihan, estimasi_kekar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        gender = request.form["gender"]
        berat = float(request.form["berat"])
        tinggi = float(request.form["tinggi"])
        usia = int(request.form["usia"])
        aktivitas = request.form["aktivitas"]
        tujuan = request.form["tujuan"]
        hari = int(request.form["hari"])

        kalori = hitung_kalori(gender, berat, tinggi, usia, aktivitas)
        latihan = rekomendasi_latihan(tujuan)
        estimasi = estimasi_kekar(hari)

        return render_template(
            "result.html",
            kalori=kalori,
            latihan=latihan,
            estimasi=estimasi
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
