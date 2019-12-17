"""
In pygame, checking the keyboard state, e.g. ALT key
"""


import pygame

RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

canvas = pygame.display.set_mode((320, 240))

done = False
while not done:

    for event in pygame.event.get():

        if event.type != pygame.KEYDOWN:
            continue

        # If the ALT keys was not pressed down
        # when this event happened, skip
        # to the next event
        if not (event.mod & pygame.KMOD_ALT):
            continue

        # For Alt-R, Alt-G and Alt-B key presses,
        # turn the screen red, green or blue
        if event.key == pygame.K_r:
            canvas.fill(RED)
        elif event.key == pygame.K_g:
            canvas.fill(GREEN)
        elif event.key == pygame.K_b:
            canvas.fill(BLUE)

        # If Alt-Q was pressed, quit
        elif event.key == pygame.K_q:
            done = True

    pygame.display.flip()
