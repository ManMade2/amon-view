from flask import Blueprint, render_template, g, jsonify, Response
from .assets import getAssetsStructure, loadMap

main = Blueprint('main', __name__)

@main.route('/')
def home():

    if not hasattr(g, 'assets_structure'):
        g.assets_structure = getAssetsStructure()

    return render_template('index.html')

@main.route("/loadMap/<mapName>")
def load_map(mapName):

    map = loadMap(mapName)

    if map == None:
        return Response(f"Failed to load map '{mapName}'", status=400)

    return jsonify(map)