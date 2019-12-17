"""
Using sprites in pygame

Bouncing balls
"""


import pygame


BLACK = (0, 0, 0)

pygame.init()

canvas = pygame.display.set_mode((400, 690))


class Brick(pygame.sprite.Sprite):
    """
    Create a 'Brick' class, as a subclass of .Sprite
    """
    def __init__(self, location):
        # initialise the super (.Sprite) class
        super().__init__()

        # Create a 50 x 30 brown Surface
        # A sprite must have a .image attribute
        # The .image gets drawn when drawing the sprite
        self.image = pygame.Surface((50, 30))
        self.image.fill(pygame.color.Color('brown'))

        # A sprite must have a .rect
        # This is where the .image gets drawn
        self.rect = self.image.get_rect()

        # Move the .rect to the specified location
        self.rect = self.rect.move(location)


class Ball(pygame.sprite.Sprite):
    """
    A ball will be a blue circle, with a radius of 15
    The background has an alpha layer, so anything behind
    the area outside of the circle but within the 30 x 30 square
    can be seen 'through' the sprite's Surface
    """

    def __init__(self, location):
        super().__init__()

        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.color.Color('blue'), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(location)
        self.move_y = 10

    # The .update method gets called when calling the sprite group's
    # .update method
    def update(self):
        # If this ball collides with any brick
        if pygame.sprite.spritecollide(self, brick_spritegroup, False):
            # Change the direction
            # Start moving up instead of down
            # or, start moving down instead of up
            self.move_y = -self.move_y

        # Move the ball by the current direction and distance (10 up or down)
        self.rect.move_ip((0, self.move_y))


# These will group our bricks and balls, so we can
# place and update them with a single command
brick_spritegroup = pygame.sprite.Group()
ball_spritegroup = pygame.sprite.Group()

for i in range(6):
    # A sloping line of bricks
    # Create new bricks, place them at (15, 50), (75, 60), (165, 70), etc
    # and add them to the group
    brick_spritegroup.add(
        Brick((15 + 60 * i, 50 + 10 * i))
    )

    # A horizontal line of bricks at the bottom of the window
    brick_spritegroup.add(
        Brick((15 + 60 * i, 500))
    )

    # A horizontal line of balls, in the middle of the window
    ball_spritegroup.add(
        Ball((25 + 60 * i, 300))
    )

# Use a pygame .Clock to slow this down
clock = pygame.time.Clock()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            done = True

    canvas.fill(BLACK)

    # Draw bricks and balls
    brick_spritegroup.draw(canvas)
    ball_spritegroup.draw(canvas)

    # Show the new canvas
    pygame.display.flip()

    # Call the .update method of each ball
    # This will move them up and/or down
    ball_spritegroup.update()

    # Wait a little bit if necessary
    # so this will 30 times per second
    # i.e. 30 frames per second (fps)
    clock.tick(30)
