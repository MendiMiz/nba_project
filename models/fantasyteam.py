from dataclasses import dataclass


@dataclass
class FantasyTeam:
    name: str
    C: str
    PF: str
    SF: str
    SG: str
    PG: str
    id: int = None