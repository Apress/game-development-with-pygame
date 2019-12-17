"""
pygame responding to keyboard events
"""


import pygame

BLACK = 0, 0, 0
GREEN = 0, 255, 0

canvas = pygame.display.set_mode((320, 240))

# Start with the block at 160, 120
x = 160
y = 120

# Create a green block of 20 x 20
block = pygame.Surface((20, 20))
block.fill(GREEN)

done = False
while not done:

    for event in pygame.event.get():

        if event.type != pygame.KEYDOWN:
            continue

        # If the left-arrow key is pressed, move the
        # block 10 pixels to the left
        if event.key == pygame.K_LEFT:
            x -= 10

        # Ditto for right, up and down keys
        elif event.key == pygame.K_RIGHT:
            x += 10
        elif event.key == pygame.K_UP:
            y -= 10
        elif event.key == pygame.K_DOWN:
            y += 10

        elif event.key == pygame.K_q:
            done = True

    # Remove the block by filling the screen with black
    canvas.fill(BLACK)

    # Show the block in its (new) location
    canvas.blit(block, (x, y))
    pygame.display.flip()
