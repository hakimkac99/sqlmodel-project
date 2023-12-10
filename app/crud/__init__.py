from app.models.ability import Ability, AbilityCreate, AbilityRead, AbilityUpdate
from app.models.hero import Hero, HeroCreate, HeroReadWithTeam, HeroUpdate
from app.models.link_models import (
    HeroAbilityBase,
    HeroAbilityCreateUpdate,
    HeroAbilityLink,
)
from app.models.team import Team, TeamCreate, TeamReadWithHeroes, TeamUpdate

from .base import CRUDBase

hero = CRUDBase[Hero, HeroReadWithTeam, HeroCreate, HeroUpdate](Hero)
team = CRUDBase[Team, TeamReadWithHeroes, TeamCreate, TeamUpdate](Team)
ability = CRUDBase[Ability, AbilityRead, AbilityCreate, AbilityUpdate](Ability)
hero_ability_link = CRUDBase[HeroAbilityLink, HeroAbilityBase, HeroAbilityCreateUpdate, HeroAbilityCreateUpdate](
    HeroAbilityLink
)
