from repository.seed_database import get_db_connection
from models.players_in_seasons import playersInSeason



def create_player_season(player: playersInSeason) -> int:
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO players_in_season (id, playerName, position, games, fieldGoals, fieldAttempts,
    fieldPercent, threeFg, threeAttempts, threePercent, twoFg,
    twoAttempts, twoPercent, effectFgPercent, ft, ftAttempts,
    assists, steals, blocks, turnovers,
    personalFouls, points, team, season, playerId)
        Values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
         %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id
    """, (player.id, player.player_name, player.position, player.games, player.field_goals,
    player.field_attempts, player.field_percent, player.three_fg,
    player.three_attempts, player.three_percent, player.two_fg,
    player.two_attempts, player.two_percent, player.effect_fg_percent,
    player.ft, player.ft_attempts, player.assists,
    player.steals, player.blocks, player.turnovers, player.personal_fouls,
    player.points, player.team, player.season, player.player_id))
    new_id = cursor.fetchone()['id']
    connection.commit()
    cursor.close()
    connection.close()
    return new_id

def get_all_players_seasons():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT * FROM players_in_season
    """)
    res = cursor.fetchall()
    players_in_seasons = [playersInSeason(**p) for p in res]
    return players_in_seasons
