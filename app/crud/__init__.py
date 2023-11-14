from app.models import Hero, HeroCreate, HeroRead, HeroUpdate

from .base import CRUDBase

hero = CRUDBase[Hero, HeroRead, HeroCreate, HeroUpdate](Hero)
