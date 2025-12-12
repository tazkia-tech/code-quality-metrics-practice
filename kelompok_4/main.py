from flask import Flask, render_template, request
from logika import is_prima

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    hasil = None

    if request.method == "POST":
        try:
            angka = int(request.form["angka"])
            hasil = f"{angka} Q_Q adalah bilangan prima :)" if is_prima(angka) \
                    else f"{angka} Q_Q bukan bilangan prima:P"
        except:
            hasil = "Input tidak valid."

    return render_template("index.html", hasil=hasil)

if __name__ == "__main__":
    app.run(debug=True)
