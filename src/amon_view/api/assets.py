from flask import Blueprint, jsonify, Response
from ..assets import loadMap

assets_blueprint = Blueprint('assets', __name__)

@assets_blueprint.route("/loadMap/<mapName>")
def load_map(mapName):

    map = loadMap(mapName)

    if map == None:
        return Response(f"Failed to load map '{mapName}'", status=400)

    return jsonify(map)