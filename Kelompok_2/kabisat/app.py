# app.py

from flask import Flask, render_template, request

# Inisialisasi aplikasi Flask
app = Flask(__name__)

# Fungsi logika utama
def is_leap(year):

    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False

# Rute (Route) untuk halaman utama (GET dan POST)
@app.route('/', methods=['GET', 'POST'])
def index():
    hasil = None
    tahun = None
    
    # Jika ada permintaan POST (form disubmit)
    if request.method == 'POST':
        try:
            # Ambil data dari form dengan nama 'inputTahun'
            tahun_str = request.form['inputTahun']
            tahun = int(tahun_str)
            
            # Jalankan logika Python
            if is_leap(tahun):
                hasil = f"Tahun {tahun} adalah **TAHUN KABISAT!** 🎉"
                # Kelas Tailwind untuk success
                hasil_class = "bg-green-200 text-green-800"
            else:
                hasil = f"Tahun {tahun} **BUKAN** tahun kabisat. ❌"
                # Kelas Tailwind untuk warning/failure
                hasil_class = "bg-yellow-200 text-yellow-800"

        except ValueError:
            hasil = "Mohon masukkan angka tahun yang valid."
            hasil_class = "bg-red-200 text-red-800"

    return render_template('kabisat.html', hasil=hasil, tahun=tahun, hasil_class=hasil_class if 'hasil_class' in locals() else "")

if __name__ == '__main__':
    app.run(debug=True)