from api.request_api import request_data
from utils.json_loader import load_json
from repository.seed_database import get_db_connection
# from repository.question_repository import create_question
# from service.answer_service import write_answers_to_db
# from repository.users_repository import create_user
from models.players_in_seasons import playersInSeason
# from models.Question import Question

def filter_question_answers(question):
    return {"question_text": question["question"], "correct_answer": question["correct_answer"],
            "incorrect_answers": question["incorrect_answers"]}

def players_seasons_from_api():
    seasons = ["2022", "2023", "2024"]
    data = []
    for season in seasons:
        data = data + request_data(f"http://b8c40s8.143.198.70.30.sslip.io/api/PlayerDataAdvancedPlayoffs/season/{season}")
    return data

def convert_player_season_to_model(player):
    return playersInSeason(
    playerName=player["playerName"],
    position=player["position"],
    games=player["games"],
    fieldGoals=player["fieldGoals"],
    fieldAttempts=player["fieldAttempts"],
    fieldPercent=player["fieldPercent"],
    threeFg=player["threeFg"],
    threeAttempts=player["threeAttempts"],
    threePercent=player["threePercent"],
    twoFg=player["twoFg"],
    twoAttempts=player["twoAttempts"],
    twoPercent=player["twoPercent"],
    effectFgPercent=player["effectFgPercent"],
    ft=player["ft"],
    ftAttempts=player["ftAttempts"],
    ftPercent=player["ftPercent"],
    assists=player["assists"],
    steals=player["steals"],
    blocks=player["blocks"],
    turnovers=player["turnovers"],
    personalFouls=player["personalFouls"],
    points=player["points"],
    team=player["team"],
    season=player["season"],
    playerId=player["playerId"]
)


def write_players_seasons_to_db():
    players_seasons_json = players_seasons_from_api()
    for player in players_seasons_json:
        player_season_model = convert_player_season_to_model(player)
        print(player_season_model)
        return
        # question_id = create_question(question_model)
        # write_answers_to_db(question, question_id)
    return

write_players_seasons_to_db()