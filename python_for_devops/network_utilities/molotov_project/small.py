# small.py
from flask import Flask, redirect, request

app = Flask("basic_app")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        return redirect(f"https://www.google.com/search?q={request.args.get('q','')}")
    else:
        return "<h1>GET request from Flask!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
