from flask import Blueprint, render_template, jsonify, request
from .models import assess_student_health

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    return render_template('dashboard.html')

@main.route('/assess', methods=['POST'])
def assess():
    try:
        data = request.get_json()
        exercise = float(data['exercise'])
        sleep = float(data['sleep'])
        water = float(data['water'])
        result = assess_student_health(exercise, sleep, water)
        return jsonify(result)
    except (KeyError, ValueError, TypeError) as e:
        return jsonify({"error": "Input tidak valid"}), 400