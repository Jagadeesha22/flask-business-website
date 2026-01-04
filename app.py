from flask import Flask, render_template, request
from datetime import datetime
import os

app = Flask(__name__, static_folder="static")
ENQUIRIES_FILE = os.path.join(app.root_path, "enquiries.txt")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/products")
def products():
    return render_template("products.html")
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        with open(ENQUIRIES_FILE, "a", encoding="utf-8") as f:
            f.write("=== NEW ENQUIRY ===\n")
            f.write(f"Time: {datetime.now()}\n")
            f.write(f"Name: {name}\n")
            f.write(f"Email: {email}\n")
            f.write(f"Message: {message}\n")
            f.write("------------------------------\n")

        return "<h2>Thank you! Your enquiry has been saved.</h2><a href='/contact'>Back</a>"

    return render_template("contact.html")

@app.route("/admin")
def admin():
    enquiries = []

    try:
        with open(ENQUIRIES_FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            enquiries = content.split("------------------------------")
    except FileNotFoundError:
        enquiries = []

    return render_template("admin.html", enquiries=enquiries)


if __name__ == "__main__":
    app.run(debug=False)
