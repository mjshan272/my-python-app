from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Python running in Kubernetes! MJ is uprading to CI CD DEvops"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

