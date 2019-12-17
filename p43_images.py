"""
Loading and showing images in pygame
"""


import pygame

from utils import display_and_wait


canvas = pygame.display.set_mode((500, 600))


# Load an image. This returns a Surface
# load(filename) -> Surface
castle_image = pygame.image.load('assets/carcassonne.png')

canvas.blit(castle_image, (0, 0))

display_and_wait()

lantern_image = pygame.image.load('assets/lantern.png')

for x in range(10, 500, 125):
    for y in range(10, 600, 125):
        canvas.blit(lantern_image, (x, y))

display_and_wait()

background_image = pygame.image.load('assets/sky.png')
canvas.blit(background_image, (0, 0))

# Load an image with an alpha (transparency) layer
lantern_image = pygame.image.load('assets/lantern_with_alpha_layer.png')

for x in range(10, 500, 125):
    for y in range(10, 600, 125):
        canvas.blit(lantern_image, (x, y))

display_and_wait()
