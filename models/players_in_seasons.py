from dataclasses import dataclass


@dataclass
class playersInSeason:
    playerName: str
    position: str
    age: int
    games: int
    fieldGoals: int
    fieldAttempts: int
    fieldPercent: int
    threeFg: int
    threeAttempts: int
    threePercent: float
    twoFg: int
    twoAttempts: int
    twoPercent: float
    effectFgPercent: float
    ft: int
    ftAttempts: int
    ftPercent: float
    assists: int
    steals: int
    blocks: int
    turnovers: int
    personalFouls: int
    points: int
    team: int
    season: int
    playerId: str