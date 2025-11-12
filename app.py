from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello from Flask in Docker 🚀</h1><p>This is a simple page.</p>"

@app.route("/test")
def home():
    return "<h1>TESTESTEST 🚀</h1><p>This is a simple page.</p>"

@app.route("/test2")
def home():
    return "<h1>TEST2EST2EST2 🚀</h1><p>This is a simple page.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)