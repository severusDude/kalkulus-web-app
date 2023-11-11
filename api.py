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

    if request.method == "GET":
        return render_template('calculator.html', func_mode="quadratic")

    elif request.method == "POST":

        coef_a = float(request.form['coefficient_a'])
        coef_b = float(request.form['coefficient_b'])
        coef_c = float(request.form['coefficient_c'])

        image = draw_graph("quadratic", coef_a, coef_b, coef_c)

        return render_template('calculator.html', func_mode="quadratic", graph=image)


@app.route("/cubic", methods=["GET", "POST"])
def cubic():

    if request.method == "GET":
        return render_template('calculator.html', func_mode="cubic")

    elif request.method == "POST":

        coef_a = float(request.form['coefficient_a'])
        coef_b = float(request.form['coefficient_b'])
        coef_c = float(request.form['coefficient_c'])
        coef_d = float(request.form['coefficient_d'])

        image = draw_graph("cubic", coef_a, coef_b, coef_c, coef_d)

        return render_template('calculator.html', func_mode="cubic", graph=image)


if __name__ == "__main__":
    app.run(debug=True)
