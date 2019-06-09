import enum
import sprites
import pygame

from sprite_base import SpriteBase


class LanwMower(SpriteBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.images = (sprites.LAWNMOVER_DEFAULT, sprites.LAWNMOVER_WORKING)
        self.image = self.images[self.image_idx]
        self.last_frame_time = 0
        self.working = False
        self.current_time = 0
        self.animation_time = 0.1

    def toggle_working(self):
        self.working = not self.working
        if not self.working:
            self.image = self.images[0]

    def dispatch_event(self, event):
        x_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -self.speed
            if event.key == pygame.K_RIGHT:
                x_change = +self.speed
            if event.key == pygame.K_LSHIFT:
                self.toggle_working()
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                x_change = 0
        self.move(x_change, 0)

    def update(self, dt):
        self.last_frame_time += dt
        if self.last_frame_time >= self.animation_time:
            self.last_frame_time = 0
            if self.working:
                self.image_idx = (self.image_idx + 1) % 2
                self.image = self.images[self.image_idx]


def get_lawn_mower(screen, *args, **kwargs):
    return LanwMower(
        screen=screen,
        left_offset=32,
        top_offset=72,
        right_offset=40,
        bottom_offset=64,
        width=sprites.SPRITE_WIDTH,
        height=sprites.SPRITE_HEIGHT,
        **kwargs
    )
