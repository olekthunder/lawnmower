import pygame
import colors
from lawnmower import LanwMower

DISPLAY_WIDTH, DISPLAY_HEIGHT = 800, 600


def init_screen(width, height):
    pygame.init()
    pygame.display.set_caption("Lanwfuckingmower")
    return pygame.display.set_mode((width, height))


def loop():
    screen = init_screen(DISPLAY_WIDTH, DISPLAY_HEIGHT)
    lawnmower = LanwMower()

    # Temp shit
    x = 100
    y = 300
    x_change = 0
    y_change = 0

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    y_change = -5
                if event.key == pygame.K_DOWN:
                    y_change = 5
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    x_change = 0
                if event.key in (pygame.K_UP, pygame.K_DOWN):
                    y_change = 0
            print(x, y)

            future_x = x + x_change
            future_y = y + y_change
            if future_x < DISPLAY_WIDTH - lawnmower.width and future_x > 0:
                x = future_x
            if future_y < DISPLAY_HEIGHT - lawnmower.height and future_y > 0:
                y = future_y
            screen.fill(colors.WHITE)
            lawnmower.show(screen, x, y)

            pygame.display.update()
    return


if __name__ == "__main__":
    loop()  # Wait for it...

    # Quit
    pygame.quit()
    quit()
