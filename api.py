from flask import Flask, session, render_template, request
from main import *

app = Flask(__name__)
app.secret_key = "BAD_SECRET_KEY"


@app.route("/", methods=["GET"])
def hello():
    session.clear()
    return render_template('home.html')


@app.route("/linear", methods=["GET", "POST"])
def linear():

    if request.method == "GET":
        return render_template('calculator.html', func_mode="linear")

    elif request.method == "POST":

        func01_information = get_form_data(multi_query=True)
        result = draw_graph("linear", *func01_information['coef'])

        # create 'linear_func' item if it doesn't exist within session data
        if 'linear_func' not in session:
            session['linear_func'] = {'func_1': func01_information}

        else:
            session['linear_func'].update(
                {f"func_{len(session['linear_func'])+1}": func01_information})

            # to make sure the updated session is saved
            session.modified = True

        image, func_detail = draw_multi_graph(
            "linear", session.get('linear_func'))

        return render_template('calculator.html', func_mode="linear", graph=image, points=result[1], func_expr=result[2])


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


def get_form_data(multi_query=True):
    """Loop through posted form data and return it"""

    data = ()
    func_information = {}

    for value in request.form.values():
        data = (*data, float(value))

    if multi_query:
        func_information['coef'] = data

        return func_information

    return data


if __name__ == "__main__":
    app.run(debug=True)
