from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <title>Mood Temen Analyzer - BEFORE</title>
</head>
<body>
    <h1>👫 Mood Temen Analyzer (Before)</h1>

    <form id="friendForm">
        <label>Seberapa sering dia bales chat (0-10)</label>
        <input type="number" id="reply_freq">

        <label>Jumlah emoji yang dipakai (0-10)</label>
        <input type="number" id="emoji_count">

        <label>Tingkat slow respons (0-10)</label>
        <input type="number" id="response_time">

        <button type="submit">Cek Mood</button>
    </form>

    <div id="result"></div>

<script>
document.getElementById("friendForm").addEventListener("submit", async (e) => {
    e.preventDefault();
    const data = {
        reply_freq: Number(document.getElementById("reply_freq").value),
        emoji_count: Number(document.getElementById("emoji_count").value),
        response_time: Number(document.getElementById("response_time").value)
    };
    const res = await fetch("/mood", {
        method:"POST",
        headers:{ "Content-Type":"application/json" },
        body: JSON.stringify(data)
    });
    const result = await res.json();
    document.getElementById("result").innerHTML = JSON.stringify(result)
})
</script>

</body>
</html>
"""


@app.route("/mood", methods=["POST"])
def mood():
    data = request.get_json()
    r = float(data["reply_freq"])
    e = float(data["emoji_count"])
    t = float(data["response_time"])

    score = (
        0.4*(min(r/10,1)) +
        0.4*(min(e/10,1)) +
        0.2*(1 - min(t/10,1))
    )

    if score >= .8: mood="Happy"; emoji="😄"
    elif score >= .6: mood="Fine"; emoji="🙂"
    elif score >= .4: mood="Slow"; emoji="😐"
    else: mood="Annoyed"; emoji="😒"

    return jsonify({"score": round(score,2), "mood":mood, "emoji":emoji})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
