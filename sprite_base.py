import pygame
import colors


class SpriteBase(pygame.sprite.Sprite):
    image = pygame.Surface([80, 80]).fill(colors.WHITE)

    def __init__(
        self, screen, image=None, x=0, y=0, width=0, height=0, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.image = image or self.image
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y - self.height
        self.screen = screen
        self.image_idx = 0

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

    def render(self):
        self.screen.blit(self.image, (self.x, self.y))

    def move(self, x_change=0, y_change=0):
        new_x = self.x + x_change
        new_y = self.y + y_change
        if not self.will_limits_be_exceeded(new_x, new_y):
            self.x = new_x
            self.y = new_y
        else:
            self.on_limits_exceeded_callback()

    def will_limits_be_exceeded(self, new_x, new_y):
        display_width, display_height = self.screen.get_size()
        return (
            new_x > display_width - self.width
            or new_x < 0
            or new_y > display_height - self.height
            or new_y < 0
        )

    def on_limits_exceeded_callback(self):
        pass

    def update(self, *args):
        self.render()

    def next_image(self, *args, **kwargs):
        pass

    def dispatch_event(self, event):
        pass
