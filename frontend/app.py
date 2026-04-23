from flask import Flask, request, render_template_string
import requests

app = Flask(__name__)

HTML = """
<h2>Survey</h2>
<form method="post">
Q1: Capital of France?<br>
<input name="q1"><br>
Q2: 2+2?<br>
<input name="q2"><br>
Q3: Sun rises from?<br>
<input name="q3"><br>
Q4: Largest ocean?<br>
<input name="q4"><br>
Q5: Fastest animal?<br>
<input name="q5"><br><br>
<input type="submit">
</form>
"""

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        data = request.form.to_dict()
        requests.post("http://backend-service:5000/save", json=data)
        return "Submitted!"
    return HTML

app.run(host="0.0.0.0", port=5000)
