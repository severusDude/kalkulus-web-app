from flask import Flask, session, render_template, request, jsonify, redirect, url_for
from main import *

app = Flask(__name__)
app.secret_key = "BAD_SECRET_KEY"


@app.route("/", methods=["GET"])
def hello():
    return render_template('home.html')


@app.route("/linear", methods=["GET", "POST", "PUT", "DELETE"])
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

        # set default function options
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

        return redirect(url_for('linear'))

    elif request.method == "PUT":
        updated_func_information = request.get_json()

        # Process the updated function data received and update session data
        for func_id, func_data in updated_func_information.items():
            session['linear_func'][func_id]['show'] = func_data['show']
            session['linear_func'][func_id]['marker'] = func_data['marker']
            session['linear_func'][func_id]['color'] = func_data['color']

            session.modified = True

        # redraw the graph
        image, func_detail = draw_multi_graph(
            "linear", session.get('linear_func'))

        # return need to be in form of json
        return jsonify({'image': image})

    elif request.method == "DELETE":

        session.pop('linear_func', None)
        session.modified = True

        return redirect(url_for('linear'), code=303)


@app.route("/quadratic", methods=["GET", "POST", "PUT", "DELETE"])
def quadratic():

    if request.method == "GET":
        if 'quadratic_func' not in session:
            return render_template('calculator.html', func_mode="quadratic")
        else:
            image, func_detail = draw_multi_graph(
                "quadratic", session.get('quadratic_func'))
            return render_template('calculator.html', func_mode="quadratic", graph=image, func_detail=func_detail, func_information=session.get('quadratic_func'))

    elif request.method == "POST":

        func02_information = get_form_data(multi_query=True)

        # set default function options
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

        return redirect(url_for('quadratic'))

    elif request.method == "PUT":
        updated_func_information = request.get_json()

        # Process the updated function data received and update session data
        for func_id, func_data in updated_func_information.items():
            session['quadratic_func'][func_id]['show'] = func_data['show']
            session['quadratic_func'][func_id]['marker'] = func_data['marker']
            session['quadratic_func'][func_id]['color'] = func_data['color']

            session.modified = True

        # redraw the graph
        image, func_detail = draw_multi_graph(
            "quadratic", session.get('quadratic_func'))

        # return need to be in form of json
        return jsonify({'image': image})

    elif request.method == "DELETE":

        session.pop('quadratic_func', None)
        session.modified = True

        return redirect(url_for('quadratic'), code=303)


@app.route("/cubic", methods=["GET", "POST", "PUT", "DELETE"])
def cubic():

    if request.method == "GET":
        if 'cubic_func' not in session:
            return render_template('calculator.html', func_mode="cubic")
        else:
            image, func_detail = draw_multi_graph(
                "cubic", session.get('cubic_func'))
            return render_template('calculator.html', func_mode="cubic", graph=image, func_detail=func_detail, func_information=session.get('cubic_func'))

    elif request.method == "POST":

        func03_information = get_form_data(multi_query=True)

        # set default function options
        func03_information.update({
            'show': True,
            'marker': True,
            'color': 'blue'
        })

        # create 'cubic_func' item if it doesn't exist within session data
        if 'cubic_func' not in session:
            session['cubic_func'] = {'func_1': func03_information}

        else:
            session['cubic_func'].update(
                {f"func_{len(session['cubic_func'])+1}": func03_information})

            # to make sure the updated session is saved
            session.modified = True

        image, func_detail = draw_multi_graph(
            "cubic", session.get('cubic_func'))

        return redirect(url_for('cubic'))

    elif request.method == "PUT":
        updated_func_information = request.get_json()

        # Process the updated function data received and update session data
        for func_id, func_data in updated_func_information.items():
            session['cubic_func'][func_id]['show'] = func_data['show']
            session['cubic_func'][func_id]['marker'] = func_data['marker']
            session['cubic_func'][func_id]['color'] = func_data['color']

            session.modified = True

        # redraw the graph
        image, func_detail = draw_multi_graph(
            "cubic", session.get('cubic_func'))

        # return need to be in form of json
        return jsonify({'image': image})

    elif request.method == "DELETE":

        session.pop('cubic_func', None)
        session.modified = True

        return redirect(url_for('cubic'), code=303)


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
