from flask import Flask, render_template, request
from main import *

app = Flask(__name__)


@app.route("/", methods=["GET"])
def hello():
    return render_template('home.html')


@app.route("/linear", methods=["GET", "POST"])
def linear():

    if request.method == "GET":
        return render_template('calculator.html', func_mode="linear")

    elif request.method == "POST":

        coef = float(request.form['coefficient'])
        const = float(request.form['constant'])

        image = draw_graph("linear", coef, const)

        return render_template('calculator.html', func_mode="linear", graph=image)


@app.route("/quadratic", methods=["GET", "POST"])
def quadratic():
    return render_template('calculator.html', func_mode="quadratic")


if __name__ == "__main__":
    app.run(debug=True)
