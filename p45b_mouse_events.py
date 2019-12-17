"""
Handling mouse events in pygame

Drag and drop an image
"""


import pygame


BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255

pygame.init()
canvas = pygame.display.set_mode((500, 600))


people = pygame.image.load('assets/people.png')

# Start with image at 0, 0
people_rect = people.get_rect()

# Are we dragging the image?
dragging = False

done = False
while not done:
    # Blank canvas
    canvas.fill(BLACK)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():

        # If mouse button pressed,
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the mouse pointer is on top
            # of the image
            if people_rect.collidepoint(mouse_x, mouse_y):

                # Start dragging
                dragging = True

        # If the mouse button was released, stop dragging
        elif event.type == pygame.MOUSEBUTTONUP:
            dragging = False

        # Exit when 'q' is pressed
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            done = True

    # When dragging, move the image to the current
    # mouse position
    if dragging:
        people_rect.left = mouse_x
        people_rect.top = mouse_y

    # Show the image at the (new) location
    canvas.blit(people, people_rect)

    pygame.display.flip()
