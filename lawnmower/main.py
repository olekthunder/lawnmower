import pygame
from . import colors
from .lawnmower import get_lawn_mower
from .grass import init_grass_array

pygame.init()

HELP = {
    "H": "Hide help",
    "Q": "Quit",
    "G": "Refresh grass",
    "R": "Refill fuel",
    "Left/Right": "Move lawnmower",
    "Down": "Stop the lawnmower",
    "L_SHIFT": "Run (stop) lawnmower",
}

DISPLAY_WIDTH, DISPLAY_HEIGHT = 1024, 600
Y_OFFSET = 512
FPS = 60
FONT_SIZE = 20
SPACING = 2
FONT = pygame.font.SysFont("Fira Code", FONT_SIZE)


def init_screen(width, height):
    pygame.display.set_caption("Lanwfuckingmower")
    return pygame.display.set_mode((width, height))


def repaint_bg(screen, show_help=False):
    sky_rectangle = pygame.Rect(0, 0, DISPLAY_WIDTH, Y_OFFSET)
    ground_rectangle = pygame.Rect(
        0, Y_OFFSET, DISPLAY_WIDTH, DISPLAY_HEIGHT - Y_OFFSET
    )
    screen.fill(colors.BLACK, rect=sky_rectangle)
    screen.fill(colors.BROWN, rect=ground_rectangle)
    if show_help:
        for i, key in enumerate(HELP):
            screen.blit(
                FONT.render(f"{key:>10}  {HELP[key]}", True, colors.WHITE),
                (20, (FONT_SIZE + SPACING) * i + 20),
            )
    else:
        screen.blit(FONT.render("Press H for help", True, colors.WHITE), (20, 20))


def loop():
    show_help = False
    screen = init_screen(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    clock = pygame.time.Clock()
    lawnmower = get_lawn_mower(screen, x=64, y=Y_OFFSET + 48)
    all_sprites = pygame.sprite.Group()
    grass_array = init_grass_array(screen, x=64, y=Y_OFFSET + 48)
    all_sprites.add(lawnmower, *grass_array)

    # Game loop
    while True:
        dt = clock.tick(FPS) / 1000

        # Events
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            # Quit
            if event.key == pygame.K_q:
                return
            # Refresh grass
            if event.key == pygame.K_g:
                for g in grass_array:
                    g.cut = False
            # Toggle help
            if event.key == pygame.K_h:
                show_help = not show_help
        # WM_CLOSE (quit)
        if event.type == pygame.QUIT:
            return
        lawnmower.dispatch_event(event)

        # Render
        repaint_bg(screen, show_help=show_help)
        for i, grass in enumerate(grass_array):
            if lawnmower.working and grass.rect.colliderect(lawnmower.rect):
                grass.cut = True
            else:
                grass.render()

        # Update
        all_sprites.update(dt)
        pygame.display.update()


def run():
    loop()  # Wait for it...

    # Quit
    pygame.quit()
    quit()


if __name__ == "__main__":
    run()
