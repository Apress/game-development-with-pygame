"""
Image transformations in pygame
"""


import pygame

from utils import display_and_wait

BLACK = 0, 0, 0

canvas = pygame.display.set_mode((500, 600))


# Load an image - size: 400 x 218
landscape = pygame.image.load('assets/landscape.png')
canvas.blit(landscape, (0, 0))
display_and_wait('Original image')

# Create a scaled copy of the image, size 500 x 100, i.e. wider
# .scale(image, (width, height))
wide_landscape = pygame.transform.scale(landscape, (500, 100))
canvas.blit(wide_landscape, (0, 250))
display_and_wait('Scale - wide')

# Create a scaled copy of the image, size 100 x 218, i.e. more narrow
narrow_landscape = pygame.transform.scale(landscape, (100, 218))
canvas.blit(narrow_landscape, (0, 370))
display_and_wait('Scale - narrow')

canvas.fill(BLACK)

courtyard = pygame.image.load('assets/courtyard.png')
canvas.blit(courtyard, (0, 0))
display_and_wait('Original image')


# Copy of image flipped along y-axis, i.e. upside down
# .flip(Surface, xbool, ybool) -> Surface
upside_down_courtyard = pygame.transform.flip(courtyard, False, True)
canvas.blit(upside_down_courtyard, (0, 250))
display_and_wait('Vertical flip')

# Copy of image flipped along x-axis, i.e. left to right
left_to_right_courtyard = pygame.transform.flip(courtyard, True, False)
canvas.blit(left_to_right_courtyard, (0, 250))
display_and_wait('Horizontal flip')

# Copy of image flipped along both axes, same as 180 degree rotation
both_flipped_courtyard = pygame.transform.flip(courtyard, True, True)
canvas.blit(both_flipped_courtyard, (0, 250))
display_and_wait('Horizontal and vertical flip')

canvas.fill(BLACK)

arrow = pygame.image.load('assets/arrow.png')
canvas.blit(arrow, (0, 0))
display_and_wait('Original image')

# Copy of image rotated 15 degrees counter clockwise
# .rotate(Surface, angle) -> Surface
arrow_15 = pygame.transform.rotate(arrow, 15)
canvas.blit(arrow_15, (100, 0))
display_and_wait('Rotate by 15 degrees, counterclockwise')

# Copy of image rotated 15 degrees counter clockwise
# Plus bounding (surrounding) box
arrow_15 = pygame.transform.rotate(arrow, 15)
bounding_box = pygame.Surface(arrow_15.get_rect().size)
bounding_box.fill(pygame.Color('white'))
canvas.blit(bounding_box, (100, 0))
canvas.blit(arrow_15, (100, 0))
display_and_wait('Rotate by 15 degrees, with bounding box')

# Copy of image rotated 45 degrees clockwise
arrow_minus_45 = pygame.transform.rotate(arrow, -45)
canvas.blit(arrow_minus_45, (200, 0))
display_and_wait('Rotate by 45 degrees')

# Multiple copies of image, rotated at 0, 15, 30, ... 345 degrees counterclockwise
# All placed with top left hand corner at 0, 200
arrow = pygame.image.load('assets/arrow2.png')
for i in range(0, 360, 15):
    canvas.blit(
        pygame.transform.rotate(arrow, i),
        (0, 200)
        )

display_and_wait('Rotate multiple times, in steps of 15 degrees')


# Multiple copies of image, rotated at 0, 15, 30, ... 345 degrees counterclockwise
# All placed with the center at 200, 400
for i in range(0, 360, 15):
    new_arrow = pygame.transform.rotate(arrow, i)
    rect = new_arrow.get_rect()
    rect.center = (200, 400)

    canvas.blit(new_arrow, rect)

display_and_wait('Rotate multiple times, in steps of 15 degrees, placement based on center')
