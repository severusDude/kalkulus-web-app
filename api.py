from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return "Server Activate"


if __name__ == "__main__":
    app.run(debug=True)
