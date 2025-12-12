from flask import Blueprint, render_template, jsonify, request
from app.models import lifestyle_score  # pastikan core.py ada di app/

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    # Halaman sederhana dengan form lifestyle
    return render_template('dashboard.html')

@main.route('/assess-lifestyle', methods=['POST'])
def assess_lifestyle():
    try:
        data = request.get_json(force=True)
        nongkrong = float(data.get('nongkrong', 0))
        hiburan = float(data.get('hiburan', 0))
        belajar = float(data.get('belajar', 0))
        kerja = float(data.get('kerja', 0))
        result = lifestyle_score(nongkrong, hiburan, belajar, kerja)
        return jsonify(result)
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({"error": "Input tidak valid", "detail": str(e)}), 400
