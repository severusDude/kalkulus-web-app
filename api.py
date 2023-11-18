from flask import Flask, session, render_template, request, jsonify, redirect, url_for
from main import *

app = Flask(__name__)
app.secret_key = "BAD_SECRET_KEY"


@app.route("/", methods=["GET"])
def hello():
    return render_template('home.html')


@app.route("/<function_type>", methods=["GET", "POST", "PUT", "DELETE"])
def handle_functions(function_type):
    func_session = f"{function_type}_func"

    if request.method == "GET":
        if func_session not in session:
            return render_template('calculator.html', func_mode=function_type)
        else:
            image, func_detail = draw_multi_graph(
                function_type, session.get(func_session))
            return render_template('calculator.html', func_mode=function_type, graph=image, func_detail=func_detail, func_information=session.get(func_session))

    elif request.method == "POST":

        func_information = get_form_data(multi_query=True)

        # set default function options
        func_information.update({
            'show': True,
            'marker': True,
            'color': 'blue'
        })

        # create func_session item if it doesn't exist within session data
        if func_session not in session:
            session[func_session] = {'func_1': func_information}

        else:
            session[func_session].update(
                {f"func_{len(session[func_session])+1}": func_information})

            # to make sure the updated session is saved
            session.modified = True

        return redirect(url_for('handle_functions', function_type=function_type))

    elif request.method == "PUT":
        updated_func_information = request.get_json()

        # Process the updated function data received and update session data
        for func_id, func_data in updated_func_information.items():
            session[func_session][func_id]['show'] = func_data['show']
            session[func_session][func_id]['marker'] = func_data['marker']
            session[func_session][func_id]['color'] = func_data['color']

            session.modified = True

        # redraw the graph
        image, func_detail = draw_multi_graph(
            function_type, session.get(func_session))

        # return need to be in form of json
        return jsonify({'image': image})

    elif request.method == "DELETE":

        session.pop(func_session, None)
        session.modified = True

        return redirect(url_for('handle_functions', function_type=function_type), code=303)


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
