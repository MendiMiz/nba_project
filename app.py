from flask import Flask
from routes.player_controller import player_blueprint
from repository.seed_database import create_tables, get_db_connection
from service.players_service import write_players_seasons_to_db

def create_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(player_blueprint, url_prefix="/api/players")
    return flask_app


if __name__ == "__main__":
    create_tables()
    # write_players_seasons_to_db()
    app = create_app()
    app.run(debug=True)