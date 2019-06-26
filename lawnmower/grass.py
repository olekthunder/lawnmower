from . import sprites
from .sprite_base import SpriteBase


class Grass(SpriteBase):
    DEFAULT_IMAGE = sprites.GRASS

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cut = False

    def update(self, *args, **kwargs):
        if not self.cut:
            super().update(*args, **kwargs)
