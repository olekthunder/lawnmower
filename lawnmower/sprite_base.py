import pygame

from . import colors


class SpriteBase(pygame.sprite.Sprite):
    DEFAULT_IMAGE = pygame.Surface([80, 80])
    DEFAULT_IMAGE.fill(colors.WHITE)

    def __init__(self, screen, image=None, x=0, y=0):
        super().__init__()
        self.image = image or self.DEFAULT_IMAGE
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y - self.height
        self.screen = screen

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    @property
    def x(self):
        return self.rect.x

    @x.setter
    def x(self, new_x):
        self.rect.x = new_x

    @property
    def y(self):
        return self.rect.y

    @y.setter
    def y(self, new_y):
        self.rect.y = new_y

    def move(self, x_change=0, y_change=0):
        new_x = self.x + x_change
        new_y = self.y + y_change
        if not self.will_limits_be_exceeded(new_x, new_y):
            self.x = new_x
            self.y = new_y

    def will_limits_be_exceeded(self, new_x, new_y):
        display_width, display_height = self.screen.get_size()
        return (
            new_x > display_width - self.width
            or new_x < 0
            or new_y > display_height - self.height
            or new_y < 0
        )

    def is_collide(self, other):
        return self.rect.colliderect(other.rect)

    def update(self, *args, **kwargs):
        """Hook name convention"""
        self.screen.blit(self.image, (self.x, self.y))


class AnimatedSprite(SpriteBase):
    FPS = 60

    def __init__(self, *args, images=None, animation_time=0.1, **kwargs):
        super().__init__(*args, image=self.image if not images else images[0],
                         **kwargs)
        self.image_idx = 0
        self.images = images or []
        self.image = self.image if not images else images[self.image_idx]
        self.animation_time = animation_time
        self.animation_stopped = False
        self.clock = pygame.time.Clock()
        self.last_sprite_time = 0

    def should_switch_sprite(self, now):
        return self.last_sprite_time > self.animation_time

    def next_sprite(self):
        self.image_idx = (self.image_idx + 1) % len(self.images)
        return self.images[self.image_idx]

    def get_time(self):
        return self.clock.tick(self.FPS) / 1000

    def update(self, *args, **kwargs):
        super().update(*args)
        now = self.get_time()
        self.last_sprite_time += now
        if self.should_switch_sprite(now=now):
            self.last_sprite_time = 0
            self.image = self.next_sprite()

    def stop_animation(self):
        self.image = self.images[0]
        self.image_idx = 0
