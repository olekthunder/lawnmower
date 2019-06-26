import pygame
from .sprite_base import SpriteBase
from . import colors

pygame.font.init()


class Engine(SpriteBase):
    MAX_SPEED = 32
    FONT = "Fira Code"
    FONT_SIZE = 50
    FONT = pygame.font.SysFont(FONT, FONT_SIZE)
    DEFAULT_IMAGE = pygame.Surface([10, 10], pygame.SRCALPHA, 32)

    def __init__(self, screen, fuel_consumption, *args, **kwargs):
        super().__init__(screen, *args, **kwargs)
        self.working = False
        self.fuel_consumption = fuel_consumption
        self.speed = 0
        self.acceleration = 2
        screen_width, screen_height = self.screen.get_size()
        self.x = round(screen_width * 0.6)
        self.y = round(screen_height * 0.05)

    def turn_on(self):
        self.working = True

    def turn_off(self):
        self.working = False

    def stop(self):
        self.speed = 0

    def increase_speed(self):
        if self.speed < 0:
            self.speed = 0
        else:
            new_speed = self.speed + self.acceleration
            if new_speed > self.MAX_SPEED:
                self.speed = self.MAX_SPEED
            else:
                self.speed = new_speed

    def decrease_speed(self):
        if self.speed > 0:
            self.speed = 0
        else:
            new_speed = self.speed - self.acceleration
            if new_speed < -self.MAX_SPEED:
                self.speed = -self.MAX_SPEED
            else:
                self.speed = new_speed

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.screen.blit(
            self.FONT.render(f"Speed: {abs(self.speed)}", True, colors.WHITE),
            (self.x, self.y),
        )
