from flask import Flask, request, jsonify
from Service import ToDOService
from models import Schema

import json
from bson import json_util

app = Flask(__name__)


@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, " \
                                                       "X-Requested-With "
    response.headers['Access-Control-Allow-Methods'] = "POST, GET. PUT, DELETE, OPTIONS"
    return response


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    return "Hello " + name


@app.route("/todo", methods=["GET"])
def list_todo():
    # details_dict = [doc for doc in ToDOService().list()]
    # details_json = json.dumps(details_dict, default=json_util.default)
    # return jsonify(details_json)
    return jsonify(ToDOService().list())


@app.route("/todo", methods=["POST"])
def create_todo():
    details_dict = [doc for doc in ToDOService().create(request.get_json())]
    details_json = json.dumps(details_dict, default=json_util.default)
    return jsonify(details_json)
    #return jsonify(ToDOService().create(request.get_json()))


@app.route("/todo/<item_id>", methods=["PUT"])
def update_item(item_id):
    return jsonify(ToDOService().update(item_id, request.get_json()))


@app.route("/todo/<item_id>", methods=["DELETE"])
def delete_item(item_id):
    return jsonify(ToDOService().delete(item_id))


if __name__ == "__main__":
    Schema()
    app.run(debug=True)