import pygame
import colors
from lawnmower import get_lawn_mower
from grass import init_grass_array

DISPLAY_WIDTH, DISPLAY_HEIGHT = 1024, 600
Y_OFFSET = 512
SPEED = 8  # 8px per move
FPS = 60


def init_screen(width, height):
    pygame.init()
    pygame.display.set_caption("Lanwfuckingmower")
    return pygame.display.set_mode((width, height))


def repaint_bg(screen):
    sky_rectangle = pygame.Rect(0, 0, DISPLAY_WIDTH, Y_OFFSET)
    ground_rectangle = pygame.Rect(
        0, Y_OFFSET, DISPLAY_WIDTH, DISPLAY_HEIGHT - Y_OFFSET
    )
    screen.fill(colors.BLACK, rect=sky_rectangle)
    screen.fill(colors.BROWN, rect=ground_rectangle)


def loop():
    screen = init_screen(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    clock = pygame.time.Clock()
    lawnmower = get_lawn_mower(screen, speed=8, x=64, y=Y_OFFSET)
    all_sprites = pygame.sprite.Group()
    grass_array = init_grass_array(screen, offset_x=256, offset_y=Y_OFFSET)
    all_sprites.add(lawnmower, *grass_array)

    # Game loop
    while True:
        dt = clock.tick(FPS) / 1000

        # Events
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            return
        lawnmower.dispatch_event(event)

        # Render
        repaint_bg(screen)
        for grass in grass_array:
            grass.render()
        lawnmower.render()

        # Update
        all_sprites.update(dt)
        pygame.display.update()


if __name__ == "__main__":
    loop()  # Wait for it...

    # Quit
    pygame.quit()
    quit()
