from app.models.ability import Ability, AbilityCreate, AbilityRead, AbilityUpdate
from app.models.hero import Hero, HeroCreate, HeroRead, HeroUpdate
from app.models.team import Team, TeamCreate, TeamRead, TeamUpdate

from .base import CRUDBase

hero = CRUDBase[Hero, HeroRead, HeroCreate, HeroUpdate](Hero)
team = CRUDBase[Team, TeamRead, TeamCreate, TeamUpdate](Team)
ability = CRUDBase[Ability, AbilityRead, AbilityCreate, AbilityUpdate](Ability)
