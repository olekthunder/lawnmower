import sprites
from sprite_base import SpriteBase


class Grass(SpriteBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = sprites.GRASS


def init_grass_array(screen, offset_x, offset_y, grass_sprite_size=64):
    screen_width = screen.get_width()
    return [
        Grass(
            screen=screen,
            x=x,
            y=offset_y,
            width=grass_sprite_size,
            height=grass_sprite_size,
        )
        for x in range(offset_x, screen_width, grass_sprite_size)
    ]
