from api.request_api import request_data
from repository.players_repository import create_player
from repository.players_season_repository import create_player_season
from utils.json_loader import load_json
# from service.answer_service import write_answers_to_db
# from repository.users_repository import create_user
from models.players_in_seasons import playersInSeason
from models.player import Player

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
        write_player_to_db = write_player_if_not_exists(player_season_model)
        write_player_season_to_db = create_player_season(player_season_model)
    return

