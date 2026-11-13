import os
from datetime import datetime

from flask import Flask, request, render_template_string
from markupsafe import escape

app = Flask(__name__)

LOG_FILE = os.environ.get("LOG_FILE", "log.txt")
if os.path.dirname(LOG_FILE):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

# หน้าเว็บฟอร์ม (ใช้ Jinja2 ซึ่ง escape ข้อความให้อัตโนมัติ ป้องกัน XSS)
form_html = """
<!doctype html>
<html lang="th">
<head>
  <meta charset="utf-8">
  <title>Submit Message</title>
</head>
<body>
  <h1>Submit your message</h1>
  <form method="post">
    <textarea name="message" rows="4" cols="50" required></textarea><br>
    <input type="submit" value="Submit">
  </form>

  {% if message %}
    <h2>Message received:</h2>
    <p>{{ message }}</p>
  {% endif %}

  <h2>Log ({{ log_file }})</h2>
  <pre>{{ logs }}</pre>
</body>
</html>
"""


def read_logs():
    if not os.path.exists(LOG_FILE):
        return "(ยังไม่มีข้อความ)"
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read()


@app.route("/", methods=["GET", "POST"])
def index():
    message = None
    if request.method == "POST":
        message = request.form.get("message", "").strip()
        if message:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # บันทึกลงไฟล์ log.txt (ใช้ utf-8 เพื่อรองรับภาษาไทย)
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {message}\n")
            print(f"Received: {escape(message)}", flush=True)
    return render_template_string(
        form_html, message=message, logs=read_logs(), log_file=LOG_FILE
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
