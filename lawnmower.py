import enum
import sprites
import pygame

from fuel_bar import FuelBar
from sprite_base import SpriteBase

LAWNMOWER_IMAGES = (sprites.LAWNMOVER_DEFAULT, sprites.LAWNMOVER_WORKING)

class LanwMower(SpriteBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, image=LAWNMOWER_IMAGES[0], **kwargs)
        self.last_frame_time = 0
        self.working = False
        self.current_time = 0
        self.animation_time = 0.1
        self.image_idx = 0

        self.fuel = FuelBar(
            percentage=50,
            screen=self.screen,
        )

    def run(self):
        if self.fuel:
            self.working = True

    def stop(self):
        self.working = False 
        self.image = LAWNMOWER_IMAGES[0]


    def toggle_working(self):
        if self.working:
            self.stop()
        else:
            self.run()


    def dispatch_event(self, event):
        x_change = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -self.speed
            if event.key == pygame.K_RIGHT:
                x_change = +self.speed
            if event.key == pygame.K_LSHIFT:
                self.toggle_working()
            if event.key == pygame.K_r:
                self.fuel.refill()
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
                self.fuel -= 2
                self.image = LAWNMOWER_IMAGES[self.image_idx]
                if not self.fuel:
                    self.stop()

    def render(self):
        super().render()
        self.fuel.render_bar()


def get_lawn_mower(screen, *args, **kwargs):
    return LanwMower(
        screen=screen,
        **kwargs
    )
