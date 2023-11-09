from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return render_template('home.html')


@app.route("/linear", methods=["GET", "POST"])
def linear():
    return render_template('linear.html')


@app.route("/quadratic", methods=["GET", "POST"])
def quadratic():
    return render_template('quadratic.html')


if __name__ == "__main__":
    app.run(debug=True)
