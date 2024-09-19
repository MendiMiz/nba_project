from api.request_api import request_data
from repository.players_repository import create_player
from repository.players_season_repository import create_player_season, get_players_by_position
from utils.json_loader import load_json
from models.players_in_seasons import playersInSeason
from models.player import Player
from toolz import pipe, partial

def filter_question_answers(question):
    return {"question_text": question["question"], "correct_answer": question["correct_answer"],
            "incorrect_answers": question["incorrect_answers"]}

def players_seasons_from_api():
    seasons = ["2022", "2023", "2024"]
    data = []
    for season in seasons:
        data = data + request_data(
            f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataTotals/query?season={season}&&pageSize=10"
        )
    return data


def convert_player_season_to_model(player):
    return playersInSeason(
    id=player["id"],
    player_name=player["playerName"],
    position=player["position"],
    games=player["games"],
    field_goals=player["fieldGoals"] or 0,
    field_attempts=player["fieldAttempts"],
    field_percent=player["fieldPercent"] or 0,
    three_fg=player["threeFg"],
    three_attempts=player["threeAttempts"],
    three_percent=player["threePercent"] or 0,
    two_fg=player["twoFg"],
    two_attempts=player["twoAttempts"],
    two_percent=player["twoPercent"] or 0,
    effect_fg_percent=player["effectFgPercent"] or 0,
    ft=player["ft"],
    ft_attempts=player["ftAttempts"],
    assists=player["assists"],
    steals=player["steals"],
    blocks=player["blocks"],
    turnovers=player["turnovers"],
    personal_fouls=player["personalFouls"],
    points=player["points"],
    team=player["team"],
    season=player["season"],
    player_id=player["playerId"]
)

def write_player_if_not_exists(player_season_model: playersInSeason):
    player_model = Player(id= player_season_model.player_id, player_name=player_season_model.player_name)
    player_id = create_player(player_model)
    return player_id

def write_players_seasons_to_db():
    players_seasons_json = players_seasons_from_api()
    for player in players_seasons_json:
        player_season_model = convert_player_season_to_model(player)
        player_season_model2 = add_atr_and_ppg_to_player(player_season_model)
        write_player_to_db = write_player_if_not_exists(player_season_model2)
        write_player_season_to_db = create_player_season(player_season_model2)
    return

def add_atr_and_ppg_to_player(player_season_model: playersInSeason):
    player_season_model.atr = calculate_atr(player_season_model)
    player_season_model.ppg = calculate_ppg(player_season_model)
    return player_season_model

def calculate_atr(player_season_model: playersInSeason):
    return player_season_model.assists / player_season_model.turnovers \
        if player_season_model.turnovers > 0 else player_season_model.assists

def calculate_ppg(player_season_model: playersInSeason):
    return player_season_model.points / player_season_model.games

def calculate_ppg_ratio(player_season_model: playersInSeason):
    players_in_position = get_players_by_position(player_season_model.position)
    ppg_average_season = pipe (
        players_in_position,
        partial(map, calculate_ppg),
        lambda a: sum(a) / len(a)
    )
    ppg_player = player_season_model.points / player_season_model.games
    ppg_ratio_player = ppg_player / ppg_average_season
    return ppg_ratio_player


