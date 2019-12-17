"""
Drawing shapes in pygame
"""


import pygame

from utils import display_and_wait

pygame.init()

BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255


canvas = pygame.display.set_mode((500, 600))

#### Rectangles

# .rect(surface, colour, rect (x, y, width, height), line width <optional> )
pygame.draw.rect(canvas, RED, (10, 10, 50, 50))
pygame.draw.rect(canvas, GREEN, (200, 10, 25, 25))
pygame.draw.rect(canvas, BLUE, (10, 200, 50, 10), 2)

display_and_wait('Rectangles')
canvas.fill(BLACK)


#### Circles

# .circle(surface, color, center (x, y), line width <optional> )
pygame.draw.circle(canvas, GREEN, (200, 200), 50, 5)
pygame.draw.circle(canvas, BLUE, (200, 200), 100, 20)
pygame.draw.circle(canvas, RED, (200, 200), 30)

display_and_wait('Circles')
canvas.fill(BLACK)


#### Ellipses

# Show the bounding box for the first ellipse
pygame.draw.rect(canvas, GREEN, [200, 200, 100, 50])

# .draw(canvas, color, rect (x, y, width, height), line width <optional> )
pygame.draw.ellipse(canvas, RED, [200, 200, 100, 50], 5)

pygame.draw.ellipse(canvas, BLUE, [200, 200, 50, 25], 5)
pygame.draw.ellipse(canvas, GREEN, [400, 200, 100, 50])

display_and_wait('Ellipses')
canvas.fill(BLACK)


#### Lines

# .line(surface, color, start (x, y), end (x, y), line width <optional> )
pygame.draw.line(canvas, BLUE, [0, 0], [100, 50], 5)
pygame.draw.line(canvas, RED, [100, 50], [200, 0], 5)
pygame.draw.line(canvas, GREEN, [200, 0], [300, 50])

display_and_wait('Lines')
canvas.fill(BLACK)


#### Polygons

# For a triangle, we give it three points
triangle_points = [[0, 0], [100, 0], [0, 100]]

# .polygon(surface, color, list_of_points, line_width <optional>)
pygame.draw.polygon(canvas, BLUE, triangle_points, 5)

more_points = [[100, 100], [200, 150], [200, 200], [100, 150]]
pygame.draw.polygon(canvas, RED, more_points)

display_and_wait('Polygons')

# Put a rectangle on top
pygame.draw.rect(canvas, GREEN, [80, 120, 200, 20])

display_and_wait('Overlapping rectangle')
canvas.fill(BLACK)


#### Multiple lines and circles

for i in range(0, 100, 10):
    # Vertical line at x = <i>
    pygame.draw.line(canvas, RED, [i, 0], [i, 100], 5)

    # Horizontal line at y = <i>
    pygame.draw.line(canvas, GREEN, [0, i], [100, i], 5)

for x in range(200, 300, 10):
    for y in range(200, 300, 10):
        pygame.draw.circle(canvas, BLUE, [x, y], 10)
        pygame.draw.circle(canvas, RED, [x, y], 5, 2)

display_and_wait('Multiple circles and lines')
