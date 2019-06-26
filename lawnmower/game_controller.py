import pygame

from . import colors
from .grass import Grass
from .lawnmower import get_lawn_mower

pygame.init()

DISPLAY_WIDTH, DISPLAY_HEIGHT = 1024, 600
CAPTION = "Lawnmower"

Y_OFFSET = 512
LAWNMOWER_X_OFFSET = 64
FPS = 60
FONT = "Fira Code"
FONT_SIZE = 20
SPACING = 2
FONT = pygame.font.SysFont(FONT, FONT_SIZE)


class GameController:
    HELP = {
        "H": "Hide help",
        "Q": "Quit",
        "G": "Refresh grass",
        "R": "Refill fuel",
        "Left/Right": "Move lawnmower",
        "Down": "Stop the lawnmower",
        "L_SHIFT": "Run (stop) lawnmower",
    }

    def __init__(self):
        pygame.init()
        self.screen = self.get_screen(
            caption=CAPTION, height=DISPLAY_HEIGHT, width=DISPLAY_WIDTH
        )
        self.show_help = False
        self.lawnmower = get_lawn_mower(self.screen, x=64, y=Y_OFFSET + 48)
        self.grass = [
            Grass(screen=self.screen, x=x_, y=Y_OFFSET + 48)
            for x_ in range(
                0, self.screen.get_width(), Grass.DEFAULT_IMAGE.get_rect().width
            )
        ]
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.lawnmower, *self.grass)

    @staticmethod
    def get_screen(caption, height, width):
        pygame.display.set_caption(caption)
        return pygame.display.set_mode((width, height))

    def repaint_background(self):
        sky_rectangle = pygame.Rect(0, 0, DISPLAY_WIDTH, Y_OFFSET)
        ground_rectangle = pygame.Rect(
            0, Y_OFFSET, DISPLAY_WIDTH, DISPLAY_HEIGHT - Y_OFFSET
        )
        self.screen.fill(colors.BLACK, rect=sky_rectangle)
        self.screen.fill(colors.BROWN, rect=ground_rectangle)
        if self.show_help:
            for i, key in enumerate(self.HELP):
                self.screen.blit(
                    FONT.render(
                        f"{key:>10}  {self.HELP[key]}", True, colors.WHITE
                    ),
                    (20, (FONT_SIZE + SPACING) * i + 20),
                )
        else:
            self.screen.blit(
                FONT.render("Press H for help", True, colors.WHITE),
                (20, 20)
            )

    def refresh_grass(self):
        for grass in self.grass:
            grass.cut = False

    def dispatch_event(self, event):
        if event.type == pygame.KEYDOWN:
            # Refresh grass
            if event.key == pygame.K_g:
                self.refresh_grass()
            # Toggle help
            elif event.key == pygame.K_h:
                self.show_help = not self.show_help
            # Quit
            elif event.key == pygame.K_q:
                self.quit()
            if event.key == pygame.K_DOWN:
                self.lawnmower.stop()
            if event.key == pygame.K_LEFT:
                self.lawnmower.decrease_speed()
            if event.key == pygame.K_RIGHT:
                self.lawnmower.increase_speed()
            if event.key == pygame.K_LSHIFT:
                self.lawnmower.toggle()
            if event.key == pygame.K_r:
                self.lawnmower.fuel_tank.fill_to_full()
        # WM_CLOSE (quit)
        elif event.type == pygame.QUIT:
            self.quit()

    def handle_collisions(self):
        for i, grass in enumerate(self.grass):
            if self.lawnmower.working and grass.is_collide(self.lawnmower):
                grass.cut = True

    def run(self):
        # Game loop
        while True:
            # Events
            event = pygame.event.poll()
            self.dispatch_event(event)

            # Render
            self.repaint_background()

            # Collisions
            self.handle_collisions()

            # Update
            self.all_sprites.update()
            pygame.display.update()

    @staticmethod
    def quit():
        pygame.quit()
        quit()
