from flask import Blueprint, render_template, g
from ..assets import getAssetsStructure

main_blueprint = Blueprint('main', __name__)

@main_blueprint.route('/')
def home():

    if not hasattr(g, 'assets_structure'):
        g.assets_structure = getAssetsStructure()

    return render_template('index.html')