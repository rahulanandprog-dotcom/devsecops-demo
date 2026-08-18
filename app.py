from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "DevSecOps Demo App"

@app.route("/hello")
def hello():
    name = request.args.get("name", "User")
    return f"Hello {name}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)