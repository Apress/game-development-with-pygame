"""
Using the mouse position in pygame
"""


import pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

pygame.init()
canvas = pygame.display.set_mode((500, 600))


done = False
while not done:

    # mouse.get_pos returns the current mouse position
    mouse_position = pygame.mouse.get_pos()

    print(mouse_position)

    # Clear the canvas
    canvas.fill(BLACK)

    # Draw a circle at the mouse position
    pygame.draw.circle(canvas, BLUE, mouse_position, 10, 2)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            done = True
