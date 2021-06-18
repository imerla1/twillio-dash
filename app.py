from flask import Flask, render_template, request
from dotenv import load_dotenv
from utils import fetch_sms

# load_dotenv()
app = Flask(__name__)
password = "abc123"

@app.route("/")
def index():
    # sms = fetch_sms()
    return render_template("prompt.html")

@app.route("/verify", methods=["GET", "POST"])
def verify():
    resp = request.get_json()
    pwd = resp['pwd']
    if pwd == password:
        sms = fetch_sms()

        return render_template("index.html", sms=sms)
    else:
        return f"You aren't allowed To See This Page", 400


@app.route("/query", methods=["GET", "POST"])
def query():
    pwd = request.args.get("token")
    if pwd == password:
        sms = fetch_sms()

        return render_template("index.html", sms=sms)
    else:
        return f"You aren't allowed To See This Page", 400