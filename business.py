from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/mypage/me")
def me():
    return render_template("me.html")

@app.route("/mypage/contact")
def contact():
    return render_template("contact.html")

@app.route("/mypage/contact", methods=["POST"])
def post():
    data = request.form['comment']
    print(data)
    return f"Received: '{data}'"
