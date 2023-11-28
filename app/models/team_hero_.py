from typing import List

from app.models.hero import HeroRead
from app.models.team import TeamRead


class TeamReadWithHeroes(TeamRead):
    heroes: List["HeroRead"] = []


class HeroReadWithTeam(HeroRead):
    team: TeamRead | None = None
