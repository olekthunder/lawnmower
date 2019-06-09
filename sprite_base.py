import pygame


class SpriteBase(pygame.sprite.Sprite):
    def __init__(
        self,
        screen,
        image=None,
        x=0,
        y=0,
        width=0,
        height=0,
        speed=0,
        left_offset=0,
        right_offset=0,
        top_offset=0,
        bottom_offset=0,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.screen = screen
        self.left_offset = left_offset
        self.right_offset = right_offset
        self.top_offset = top_offset
        self.bottom_offset = bottom_offset
        self.speed = speed
        self.width = width
        self.height = height
        self.image_idx = 0
        self.image = None
        self.x = x - self.left_offset
        self.y = y - (self.bottom_offset + self.top_offset)

    def render(self):
        print(self.image, self.x, self.y)
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
            new_x > display_width - self.width + self.right_offset
            or new_x < 0 - self.left_offset
            or new_y > display_height - self.height + self.top_offset
            or new_y < 0 - self.bottom_offset
        )

    def on_limits_exceeded_callback(self):
        pass

    def update(self, *args):
        pass

    def next_image(self, *args, **kwargs):
        pass

    def dispatch_event(self, event):
        pass
