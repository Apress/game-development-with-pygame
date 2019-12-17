"""
pygame game loop
"""

import pygame

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

canvas = pygame.display.set_mode((320, 240))

# Keep going until done ('q' key pressed)
done = False
while not done:

    # For each event in the queue
    for event in pygame.event.get():

        # If it is not a key_down event,
        # ignore it and check the next event
        if event.type != pygame.KEYDOWN:
            continue

        # If 'r' was pressed, fill the canvas with red
        if event.key == pygame.K_r:
            canvas.fill(RED)

        # Ditto for green and blue
        elif event.key == pygame.K_g:
            canvas.fill(GREEN)
        elif event.key == pygame.K_b:
            canvas.fill(BLUE)

        # If 'q' was pressed, set Done to True, i.e. quit
        elif event.key == pygame.K_q:
            done = True

    # Show any changes
    pygame.display.flip()
