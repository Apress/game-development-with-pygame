"""
Additional examples of drawing with shapes in pygame
"""


import math
import pygame

from utils import display_and_wait


RED = pygame.color.Color('red')
BLUE = pygame.color.Color('blue')
GREEN = pygame.color.Color('green')
WHITE = pygame.color.Color('white')
BLACK = pygame.color.Color('black')


canvas = pygame.display.set_mode((400, 690))

# Nested red squares
for i in range(10, 200, 10):
    pygame.draw.rect(canvas, RED, (5, 5, i, i), 1)

# Nested alternating blue and red squares
for i in range(100, 10, -5):
    pygame.draw.rect(canvas, RED if i % 10 else BLUE, (300 - i, 100 - i, 2 * i, 2 * i))

# Strange 'checkered' pattern
# Alternate between white and blue, depending on whether i is divisible by 20 - so every other line
for i in range(10, 201, 10):
    pygame.draw.line(canvas, WHITE if i % 20 else BLUE, (i, 300), (i, 500), 10)
for i in range(10, 201, 10):
    pygame.draw.line(canvas, WHITE if i % 20 else BLUE, (10, i + 300), (200, i + 300), 5)


display_and_wait()

canvas.fill(BLACK)

# White triangle of many lines all starting at the same point
for i in range(5, 200, 5):
    pygame.draw.line(canvas, WHITE, (0, 0), (i, 200 - i))

# Cone of nested green ellipses
for i in range(10, 200, 10):
    pygame.draw.ellipse(canvas, GREEN, (i, 250 - i, int(i/2), i * 2), 2)

# Nested blue circles
for i in range(10, 100, 10):
    pygame.draw.circle(canvas, BLUE, (150, 550), i, 1)

display_and_wait()

canvas.fill(BLACK)

# sine wave
for x in range(0, 360, 10):
    y = int(math.sin(math.radians(x)) * 150)

    # Shift and scale to fit in the window
    y = y + 170
    x = int(x * 1.7) + 50

    # Swap x and y, so the chart is on its side - to fit in the narrow window
    pygame.draw.circle(canvas, BLUE, (y, x), 8, 1)

display_and_wait()

canvas.fill(BLACK)

# spiral of circles
# Go around the circle 10 times (10 x 360 degrees)
# in steps of 10, so 36 steps per full circle
for angle in range(0, 3600, 10):
    # Calculate the position of the point
    x = int(math.sin(math.radians(angle)) * angle / 15)
    y = int(math.cos(math.radians(angle)) * angle / 15)

    # Start with (0, 255, 0), i.e. blue
    # Finish with (240, 255, 240), i.e. almost white
    # Note that 3600 / 15 = 240
    color = (angle / 15, 255, angle / 15)

    # Draw a circle at the calculated position
    # of radius 10 and a line thickness of 1
    pygame.draw.circle(canvas, BLUE, (x + 250, y + 300), 10)
    pygame.draw.circle(canvas, color, (x + 250, y + 300), 10, 1)

display_and_wait()
