import sprites


class LanwMower:
    def __init__(self):
        self.width = sprites.SPRITE_WIDTH
        self.height = sprites.SPRITE_HEIGHT
        self.working_sprite = sprites.LAWNMOVER_DEFAULT

    def show(self, screen, x, y):
        screen.blit(self.working_sprite, (x, y))
