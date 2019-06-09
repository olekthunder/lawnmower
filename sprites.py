import os
import pygame

SPRITE_WIDTH = 256
SPRITE_HEIGHT = 256
SPRITES_DIR = "sprite_images"

LAWNMOVER_DEFAULT_SPRITE_PATH = os.path.join(SPRITES_DIR, "lawnmower-default.png")
LAWNMOVER_DEFAULT = pygame.image.load(LAWNMOVER_DEFAULT_SPRITE_PATH)

LAWNMOVER_WOKRING_SPRITE_PATH = os.path.join(
    SPRITES_DIR, "lawnmower-default-working.png"
)
LAWNMOVER_WORKING = pygame.image.load(LAWNMOVER_WOKRING_SPRITE_PATH)

GRASS_SPRITE_PATH = os.path.join(SPRITES_DIR, "grass.png")
GRASS = pygame.image.load(GRASS_SPRITE_PATH)
