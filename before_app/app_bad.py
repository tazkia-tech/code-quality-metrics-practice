from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '''
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Dashboard Kesehatan (Before)</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, sans-serif;
            background-color: #f9f9fc;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 2rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        }
        h1 {
            text-align: center;
            color: #2c6fbb;
            margin-bottom: 1.5rem;
        }
        label {
            display: block;
            margin: 12px 0 6px;
            font-weight: 500;
        }
        input {
            width: 100%;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 6px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 10px;
            background: #2c6fbb;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 16px;
        }
        button:hover {
            background: #a00;
        }
        .result {
            margin-top: 20px;
            padding: 15px;
            background: #fff0f0;
            border-left: 4px solid #c00;
            border-radius: 6px;
        }
        .hidden {
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Dashboard Kesehatan Mahasiswa (Before)</h1>
        <form id="healthForm">
            <label>Jam Olahraga/Hari (jam): <input type="number" step="0.1" id="e" required></label>
            <label>Jam Tidur/Hari (jam): <input type="number" step="0.1" id="s" required></label>
            <label>Konsumsi Air/Hari (liter): <input type="number" step="0.1" id="w" required></label>
            <button type="submit">Evaluasi Kesehatan</button>
        </form>
        <div id="result" class="result hidden"></div>
    </div>

    <script>
        document.getElementById('healthForm').addEventListener('submit', async (e) => {
            e.preventDefault();
            const data = {
                e: parseFloat(document.getElementById('e').value),
                s: parseFloat(document.getElementById('s').value),
                w: parseFloat(document.getElementById('w').value)
            };
            const res = await fetch('/assess', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(data)
            });
            const result = await res.json();
            const el = document.getElementById('result');
            if (res.ok) {
                el.innerHTML = `
                    <h2>Hasil Evaluasi</h2>
                    <p>Skor: <strong>${result.score}</strong></p>
                    <p>Status: <strong>${result.status}</strong></p>
                `;
            } else {
                el.innerHTML = `<p style="color:red;">⚠️ ${result.error || 'Input tidak valid'}</p>`;
            }
            el.classList.remove('hidden');
        });
    </script>
</body>
</html>
    '''

@app.route('/assess', methods=['POST'])
def assess():
    d = request.get_json()
    try:
        e = float(d['e'])
        s = float(d['s'])
        w = float(d['w'])
        if e < 0 or s < 0 or w < 0:
            return jsonify({"error": "Nilai tidak boleh negatif"}), 400

        # Logika dalam satu fungsi besar — kode "before"
        if e >= 5 and s >= 7 and w >= 8:
            status = "Sangat Sehat"
            score = 1.0
        elif e >= 3 and s >= 6 and w >= 6:
            status = "Sehat"
            score = 0.7
        elif e >= 1 and s >= 5 and w >= 4:
            status = "Perlu Perbaikan"
            score = 0.5
        else:
            status = "Berisiko"
            score = 0.2
        return jsonify({"status": status, "score": score})
    except:
        return jsonify({"error": "Input tidak valid"}), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)