from flask import Blueprint
from crypt import methods

player_blueprint = Blueprint("player", __name__)

@player_blueprint.route('/search', methods=['GET'])
def search_player():
    new = request.args.get("mew")
    jsonify
