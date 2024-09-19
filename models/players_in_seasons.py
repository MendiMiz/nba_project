from dataclasses import dataclass


@dataclass
class playersInSeason:
    id: int
    player_name: str
    position: str
    games: int
    field_goals: int
    field_attempts: int
    field_percent: int
    three_fg: int
    three_attempts: int
    three_percent: float
    two_fg: int
    two_attempts: int
    two_percent: float
    effect_fg_percent: float
    ft: int
    ft_attempts: int
    assists: int
    steals: int
    blocks: int
    turnovers: int
    personal_fouls: int
    points: int
    team: str
    season: int
    player_id: str