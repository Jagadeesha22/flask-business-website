from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "HOME PAGE"

@app.route("/admin")
def admin():
    return "ADMIN PAGE WORKING"

app.run(port=5001)
