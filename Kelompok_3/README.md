![gambar](https://i.pinimg.com/736x/b7/31/26/b7312644e40d0355303f0889cf6fb6d3.jpg)
<h1 align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&duration=3000&pause=1000&color=00A8FF&center=true&vCenter=true&width=480&lines=+Analisis+Mood+Temen" alt="Typing SVG" />
</h1>

<p align="center"><i><strong>Tugas Kelompok Mata Kuliah Konruksi dan Rekayasa Perangkat Lunak</strong><br>Sistem Dinamis/Web-based sederhana berbasis Flask yang mencoba menebak mood temenmu</i></p>

---

## Lampiran

1. Gambaran Umum  
2. Struktur Proyek  
3. Fitur Utama  
4. Teknologi yang Digunakan  
5. Cara Menjalankan Secara Lokal  
6. Feedback dan Kontribusi  
7. Author  

---

## Gambaran Umum

**Mood Temen** adalah sistem dinamis/web-based sederhana berbasis **Flask** yang menunjukkan perbedaan antara:

- kode **Before** (1 file besar, tidak modular)  
- kode **After** (clean code, modular, reusable)

Proyek ini dibuat untuk memperlihatkan bagaimana **refactoring** dan **separation of concerns** dapat meningkatkan kualitas kode bahkan ketika topiknya sesederhana menebak mood teman 😆  

---

## Struktur Proyek

Berikut adalah arsitektur folder dan filenya:

- [group03-temen😋/](https://github.com/tazkia-tech/code-quality-metrics-practice/group03-temen😋)
  - `./requirements.txt` - Daftar Dependensi Python
- [before/](./before/)
  - `./before/app_bad.py`
- [after/](./after/)
  - `./after/run.py` – Entry point untuk menjalankan aplikasi
    - [after/app/](./after/app/)
      - `./after/app/__init__.py` – Inisialisasi aplikasi (App Factory)
      - `./after/app/models.py` – 
      - `./after/app/routes.py` – Semua logika rute & halaman
    - [after/static](./after/static/)
      - `./after/static/style.css`
    - [after/templates](./after/templates/)
      - `./after/templates/dashboard.html`
    - [after/tests](./after/tests/)
      - `./after/tests/test_models.py`
- [test/](./test/)
  - `./test/test_cli.py`

---

> _"Proyek BEFORE sengaja dibuat 'buruk' agar perbedaan terasa jelas. Proyek AFTER menunjukkan bagaimana struktur modular dapat meningkatkan reusability dan testability."_

---

## Fitur Utama

### Kalkulasi mood berdasarkan data:
- seberapa sering teman membalas chat
- jumlah emoji yang digunakan
- tingkat slow respons

### Output:
- mood
- skor
- emoji mood

### Bisa diakses dari:
- Browser (UI)
- CLI (test_cli.py)
- Unit testing

---

## Teknologi yang Digunakan

- **Backend** : Flask
- **Testing** : pytest
- **Frontend** : HTML + JS sederhana
- **Style** : CSS minimalis  

> No database, no AI, no drama… oh kecuali dramanya temen kamu 😜

---

##  Cara Menjalankan

### 1. Python & Dependencies

Pastikan Python telah terinstall, lalu jalankan:

```bash
pip install -r requirements.txt
```

### 2. Jalankan versi BEFORE (app_bad.py)

```bash
python3 before/app_bad.py
```

Lalu buka:

```bash
http://127.0.0.1:5000
```

### 3. Jalankan versi AFTER (lebih clean)

```bash
python3 after/run.py
```

Lalu buka:

```bash
http://127.0.0.1:5001
```

### 4. Jalankan dari CLI (tanpa UI)

```bash
PYTHONPATH=. python3 test/test_cli.py
```

### 5. Jalankan Unit Test

```bash
pytest
```

---

## Feedback dan Kontribusi

Kalau kamu punya ide mood lain:
- mood pacar 😳
- mood teman mabar 😅
- mood dosen 👀

Feel free buat improve atau eksperimen!

---

## Author

**zerocool979**
GitHub: [@zerocool979](https://github.com/zerocool979)

**zamarrr**
GitHub: [@zamarrr](https://github.com/zamarrr)

**shifi06**
GitHub: [@shifi06](https://github.com/shifi06)

**fitriambrsr**
GitHub: [@fitriambrsr](https://github.com/fitriambrsr)


> _"Program ini tidak menjamin temanmu beneran lagi happy. Tapi setidaknya kita punya alasan buat bercanda 😌"_ – group 03
