from types import NoneType

from repository.seed_database import get_db_connection
from models.player import Player



def create_player(player: Player) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO players (id, player_name)
        Values (%s, %s) 
        ON CONFLICT (id) DO NOTHING  
        RETURNING id;
    """, (player.id, player.player_name))
    res = cursor.fetchone()
    connection.commit()
    cursor.close()
    connection.close()
    return res