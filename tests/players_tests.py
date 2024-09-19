import pytest
from repository.seed_database import create_tables, get_db_connection
from service.players_service import write_players_seasons_to_db
from repository.players_repository import create_player
from repository.players_season_repository import  get_all_players_seasons
from models.player import Player


@pytest.fixture(scope="module")
def setup_database():
    create_tables()
    write_players_seasons_to_db()
    yield
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM players;")
    cursor.execute("""
        DROP TABLE IF EXISTS players_in_season CASCADE;
        DROP TABLE IF EXISTS players CASCADE;
        DROP TABLE IF EXISTS fantasy_team CASCADE;
    """)
    connection.commit()
    cursor.close()
    connection.close()

def test_create_player(setup_database):
    player = Player(id="donarumma_01", player_name="kjsafbkjaADNad")
    player_id = create_player(player)
    assert player_id

def test_get_all_players_seasons(setup_database):
    all_players_seasons = get_all_players_seasons()
    assert all_players_seasons

