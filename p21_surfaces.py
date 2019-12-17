"""
pygame Surfaces and Rects
"""

import pygame

from utils import display_and_wait


# Define some colours
BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

# Create the display canvas, size 500 x 600 pixels
canvas = pygame.display.set_mode((500, 600))


# Fill the canvas with 255, 0, 0 - i.e. red
canvas.fill(RED)

# Show the canvas updates (using pygame.display.flip() )
# and wait for a key or mouse button press
display_and_wait('canvas.fill(RED)')

canvas.fill(GREEN)
display_and_wait('canvas.fill(GREEN)')

# Create a new Surface, size 50 x 20
red_block = pygame.Surface([50, 20])

# Fill the block with red
red_block.fill(RED)

# 'Stamp' a copy of the block on to the canvas, at location 10, 10
canvas.blit(red_block, (10, 10))
display_and_wait('blit red_block at (10, 10)')

# Stamp another copy of the red block
canvas.blit(red_block, (100, 10))
display_and_wait('blit red_block at (100, 10)')

blue_block = pygame.Surface([100, 40])
blue_block.fill(BLUE)
canvas.blit(blue_block, (10, 100))
display_and_wait('blit blue_block at (10, 100)')

# Create a Rect instance from the Surface
# A Rect has .x, .y attributes (the position: top left hand corner)
# which is initially set to 0, 0
# and a .size attribute (also accessible as .width, .height)
# In this case the rect gets the width and height of the surface, i.e. 10 x 100
blue_rect = blue_block.get_rect()

# When blitting an image we can pass in a .Rect instance
# instead of a coordinate
canvas.blit(blue_block, blue_rect)
display_and_wait('blit blue_block at <blue_rect - (0, 0)>')

# Rect().move returns a new .Rect instance, of the same size
# but with a new .x and .y location
blue_rect = blue_rect.move([0, 200])
canvas.blit(blue_block, blue_rect)
print('blue_rect moved by [0, 200]')
display_and_wait('blit blue_block at <blue_rect - (0, 200)>')

# Use .move_ip to move the .Rect in_place,
# i.e. this changes the .Rect instead of return a new .Rect
blue_rect.move_ip([50, 0])
canvas.blit(blue_block, blue_rect)
print('blue_rect moved by [50, 0] using move_ip')
display_and_wait('blit blue_block at <blue_rect - (50, 200)>')

blue_rect.move_ip([150, 0])
canvas.blit(blue_block, blue_rect)
print('blue_rect moved by [150, 0] using move_ip')
display_and_wait('blit blue_block at <blue_rect - (200, 200)>')
