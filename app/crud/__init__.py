from app.models.hero import Hero, HeroCreate, HeroRead, HeroUpdate
from app.models.team import Team, TeamCreate, TeamRead, TeamUpdate

from .base import CRUDBase

hero = CRUDBase[Hero, HeroRead, HeroCreate, HeroUpdate](Hero)
team = CRUDBase[Team, TeamRead, TeamCreate, TeamUpdate](Team)
