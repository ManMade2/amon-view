from flask import Blueprint, render_template, jsonify, request
from jsonschema import validate, ValidationError
from ..validation.button_schema import button_schema
from ..validation.input_schema import input_schema

components_blueprint = Blueprint("components", __name__)

@components_blueprint.route("/createButton", methods=["POST"])
def create_button():

    try:
        data = request.get_json()
        validate(instance=data, schema=button_schema)
    except ValidationError as e:
        return jsonify({"error": f"Invalid input: {e.message}"}), 400

    component = render_template("components/button.html", data=data)
    return jsonify({"html": component})


@components_blueprint.route("/createInput", methods=["POST"])
def create_text_input():

    try:
        data = request.get_json()
        validate(instance=data, schema=input_schema)
    except ValidationError as e:
        return jsonify({"error": f"Invalid input: {e.message}"}), 400

    component = render_template("components/input.html", data=data)
    return jsonify({"html": component})