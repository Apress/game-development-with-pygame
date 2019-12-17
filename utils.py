"""
Utilities for the pygame demonstrations
"""


import pygame


def just_wait():
    """
    Wait until a key or mouse button has been pressed
    """
    clock = pygame.time.Clock()
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                done = True
        clock.tick(30)


def display_and_wait(info=None):
    """
    Helper function for demonstrations

    Show the canvas
    Wait for a key or mouse press
    Clear the canvas, ready for the next sample
    """
    pygame.display.flip()
    if info:
        print(info)
    print('-' * 20)

    just_wait()
