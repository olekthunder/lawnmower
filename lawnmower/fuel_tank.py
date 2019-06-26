from copy import copy

import pygame

from . import colors
from .sprite_base import SpriteBase


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
        rect = pygame.rect.Rect((0, self.HEIGHT - top_offset),
                                (self.WIDTH, top_offset))
        return pygame.draw.rect(self.image, colors.RED, rect)

    def refill(self):
        self.percentage = 100


class FuelTank(SpriteBase):
    BAR_WIDTH = 4
    BAR_HEIGHT = 200

    def __init__(self, screen, volume=100):
        super().__init__(
            screen,
            image=pygame.Surface((self.BAR_WIDTH, self.BAR_HEIGHT))
        )
        self.volume = volume
        self._fuel_left = 0
        screen_width, screen_height = self.screen.get_size()
        self.x = round(screen_width * 0.95)
        self.y = round(screen_height * 0.05)

    @property
    def fuel_left(self):
        return self._fuel_left

    @property
    def empty(self):
        return bool(self.fuel_left)

    @property
    def percentage(self):
        return (self.fuel_left / self.volume) * 100

    def fill(self, amount):
        total_fuel = amount + self.fuel_left
        self._fuel_left = (
            total_fuel
            if total_fuel < self.volume
            else self.volume
        )

    def fill_to_full(self):
        self.fill(self.volume)

    def use(self, amount):
        assert amount >= 0, amount
        new_amount = self._fuel_left - amount
        self._fuel_left = 0 if self._fuel_left < 0 else new_amount

    def draw_left_fuel_bar(self):
        top_offset = round(self.BAR_HEIGHT * self.percentage / 100)
        rect = pygame.rect.Rect(
            (0, self.BAR_HEIGHT - top_offset),
            (self.BAR_WIDTH, top_offset)
        )
        pygame.draw.rect(self.image, colors.RED, rect)

    def update(self, *args, **kwargs):
        self.image.fill(colors.WHITE)
        self.draw_left_fuel_bar()
        super().update(*args, **kwargs)
