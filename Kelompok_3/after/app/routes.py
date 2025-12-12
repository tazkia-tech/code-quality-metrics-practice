from flask import Blueprint, request, jsonify, render_template
from .models import assess

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("dashboard.html")

@main.route("/mood", methods=["POST"])
def mood():
    try:
        data = request.get_json()
        r = float(data["reply_freq"])
        e = float(data["emoji_count"])
        t = float(data["response_time"])
        return jsonify(assess(r, e, t))
    except:
        return jsonify({"error": "Input tidak valid"}), 400
