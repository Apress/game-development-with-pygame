"""
pygame colors
"""

import pygame

from utils import display_and_wait


canvas = pygame.display.set_mode((500, 600))

# Blank canvas
display_and_wait('Blank canvas')

# White, using (R, G, B)
canvas.fill((255, 255, 255))
display_and_wait('White - (255, 255, 255)')

# Red, using (R, G, B)
canvas.fill((255, 0, 0))
display_and_wait('Red - (255, 0, 0)')

# Green, using a constant
GREEN = (0, 255, 0)
canvas.fill(GREEN)
display_and_wait('GREEN - (0, 255, 0)')

# Named color, for a specific purpose
WARNING_COLOR = (255, 0, 0)
canvas.fill(WARNING_COLOR)
display_and_wait('WARNING_COLOR - (255, 0, 0)')

# pygame's colors
# For list, go to
# https://github.com/pygame/pygame/blob/master/src_py/colordict.py
canvas.fill(pygame.Color('gold'))
display_and_wait("Gold - pygame.Color('gold')")
