import pygame
import colors

from copy import copy
from sprite_base import SpriteBase


class FuelBar(SpriteBase):
    WIDTH = 4
    HEIGHT = 200

    def __init__(self, *args, percentage=0, **kwargs):
        super().__init__(
            *args, image=pygame.Surface((self.WIDTH, self.HEIGHT)), **kwargs
        )
        screen_width, screen_height = self.screen.get_size()
        self.x = round(screen_width * 0.95)
        self.y = round(screen_height * 0.05)
        self._percentage = percentage
        self.fuel_left_bar_rect = self.draw_left_fuel_bar(percentage)
        self.update()

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, new):
        self._percentage = new if new > 0 else 0

    def update(self):
        self.image.fill(colors.WHITE)
        self.fuel_left_bar_rect = self.draw_left_fuel_bar(self.percentage)

    def render_bar(self):
        self.update()
        super().render()

    def draw_left_fuel_bar(self, percentage):
        top_offset = round(self.HEIGHT * percentage / 100)
        rect = pygame.rect.Rect((0, self.HEIGHT - top_offset), (self.WIDTH, top_offset))
        return pygame.draw.rect(self.image, colors.RED, rect)

    def refill(self):
        self.percentage = 100

    def __add__(self, percents):
        new = copy(self)
        new.percentage += percents
        return new

    def __iadd__(self, percents):
        self.percentage += percents
        return self

    def __isub__(self, percents):
        self.percentage -= percents
        return self

    def __sub__(self, percents):
        new = copy(self)
        new.percentage -= percents
        return new

    def __bool__(self):
        return bool(self.percentage)
