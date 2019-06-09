import os
import pygame

SPRITE_WIDTH = 256
SPRITE_HEIGHT = 256
SPRITES_DIR = "sprite_images"

LAWNMOVER_DEFAULT_SPRITE_PATH = os.path.join(SPRITES_DIR, 'lawnmower-default.png')
LAWNMOVER_DEFAULT = pygame.image.load(LAWNMOVER_DEFAULT_SPRITE_PATH)
