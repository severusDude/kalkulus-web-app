from flask import Flask, session, render_template, request, jsonify
from main import *

app = Flask(__name__)
app.secret_key = "BAD_SECRET_KEY"


@app.route("/", methods=["GET"])
def hello():
    session.clear()
    return render_template('home.html')


@app.route("/linear", methods=["GET", "POST", "PUT"])
def linear():

    if request.method == "GET":
        if 'linear_func' not in session:
            return render_template('calculator.html', func_mode="linear")
        else:
            image, func_detail = draw_multi_graph(
                "linear", session.get('linear_func'))
            return render_template('calculator.html', func_mode="linear", graph=image, func_detail=func_detail, func_information=session.get('linear_func'))

    elif request.method == "POST":

        func01_information = get_form_data(multi_query=True)

        func01_information.update({
            'show': True,
            'marker': True,
            'color': 'blue'
        })

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

        return render_template('calculator.html', func_mode="linear", graph=image, func_detail=func_detail, func_information=session.get('linear_func'))

    elif request.method == "PUT":
        updated_func_information = request.get_json()

        # Process the updated function data received
        for func_id, func_data in updated_func_information.items():
            session['linear_func'][func_id]['show'] = func_data['show']
            session['linear_func'][func_id]['marker'] = func_data['marker']
            session['linear_func'][func_id]['color'] = func_data['color']

            session.modified = True

        image, func_detail = draw_multi_graph(
            "linear", session.get('linear_func'))

        return jsonify({'image': image})


@app.route("/quadratic", methods=["GET", "POST", "PUT"])
def quadratic():

    if request.method == "GET":
        return render_template('calculator.html', func_mode="quadratic")

    elif request.method == "POST":

        func02_information = get_form_data(multi_query=True)

        func02_information.update({
            'show': True,
            'marker': True,
            'color': 'blue'
        })

        # create 'quadratic_func' item if it doesn't exist within session data
        if 'quadratic_func' not in session:
            session['quadratic_func'] = {'func_1': func02_information}

        else:
            session['quadratic_func'].update(
                {f"func_{len(session['quadratic_func'])+1}": func02_information})

            # to make sure the updated session is saved
            session.modified = True

        image, func_detail = draw_multi_graph(
            "quadratic", session.get('quadratic_func'))

        return render_template('calculator.html', func_mode="quadratic", graph=image, func_detail=func_detail, func_information=session.get('quadratic_func'))

    elif request.method == "PUT":
        updated_func_information = request.get_json()

        # Process the updated function data received
        for func_id, func_data in updated_func_information.items():
            session['quadratic_func'][func_id]['show'] = func_data['show']
            session['quadratic_func'][func_id]['marker'] = func_data['marker']
            session['quadratic_func'][func_id]['color'] = func_data['color']

            session.modified = True

        image, func_detail = draw_multi_graph(
            "quadratic", session.get('quadratic_func'))

        return jsonify({'image': image})


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
