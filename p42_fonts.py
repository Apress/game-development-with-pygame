"""
Using fonts to show text in pygame
"""


import pygame

from utils import display_and_wait


BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

pygame.init()
canvas = pygame.display.set_mode((500, 600))

# Create a new pygame Font instance, Arial 24
# SysFont(name, size, bold=False, italic=False) -> Font
font = pygame.font.SysFont('Arial', 24)

# Create a new pygame Surface instance,
# which contains the rendered text
# render(text, antialias, color, background=None) -> Surface
text_surface = font.render('Some text, in Arial 24', True, WHITE)

# 'Stamp' the text on to the display Surface
canvas.blit(text_surface, (20, 20))
display_and_wait('Arial 24 at (20,20)')

# Stamp the text a few more times on to the display Surface
for y in range(20, 300, 50):
    canvas.blit(text_surface, (20, y))
display_and_wait('More lines, same font')

# Create an italic text surface and stamp it on to the display Surface
italic_font = pygame.font.SysFont('Arial', 24, italic=True)
text_surface = italic_font.render('Italic text, still in Arial 24', True, GREEN)
canvas.blit(text_surface, (20, 320))

display_and_wait('Italic 24 at (20, 320)')
