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

        coef = get_form_data()
        result = draw_graph("linear", *coef)

        return render_template('calculator.html', func_mode="linear", graph=result[0], points=result[1], func_expr=result[2])


@app.route("/quadratic", methods=["GET", "POST"])
def quadratic():

    if request.method == "GET":
        return render_template('calculator.html', func_mode="quadratic")

    elif request.method == "POST":

        coef = get_form_data()
        result = draw_graph("quadratic", *coef)

        return render_template('calculator.html', func_mode="quadratic", graph=result[0], points=result[1], func_expr=result[2])


@app.route("/cubic", methods=["GET", "POST"])
def cubic():

    if request.method == "GET":
        return render_template('calculator.html', func_mode="cubic")

    elif request.method == "POST":

        coef = get_form_data()
        result = draw_graph("cubic", *coef)

        return render_template('calculator.html', func_mode="cubic", graph=result[0], points=result[1], func_expr=result[2])


def get_form_data():
    """Loop through posted form data and return it"""

    data = ()

    for value in request.form.values():
        data = (*data, float(value))

    return data


if __name__ == "__main__":
    app.run(debug=True)
