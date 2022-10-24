from flask import Flask, render_template, request, make_response, jsonify
import requests
import random
app = Flask(__name__, instance_relative_config=True)

@app.route('/rand')
def rand():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a and b:
        output = random.randint(a, b)
        return make_response(jsonify(output), 200) # HTTP 200 OK
    else:
        return make_response('Invalid input\n', 400) # HTTP 400 BAD REQUEST


def create_app():
    return app
