from flask import Blueprint, request, jsonify
from repository.players_season_repository import get_players_by_position


player_blueprint = Blueprint("players", __name__)

@player_blueprint.route('/search', methods=['GET'])
def search_player():
    position = request.args.get("position")
    players_in_position = get_players_by_position(position)
    return jsonify(players_in_position), 200
