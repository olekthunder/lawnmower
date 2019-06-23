import sprites
from sprite_base import SpriteBase


class Grass(SpriteBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, image=sprites.GRASS, **kwargs)
        self.cut = False

    def render(self):
        if not self.cut:
            super().render()


def init_grass_array(screen, x, y, grass_sprite_size=64):
    screen_width = screen.get_width()
    return [
        Grass(
            screen=screen, x=x, y=y, width=grass_sprite_size, height=grass_sprite_size
        )
        for x in range(x, screen_width, grass_sprite_size)
    ]
