"""
Playing sound effects in pygame

Bouncy balls with bounce sound

For more comments see p46_sprites
"""


import pygame


BLACK = (0, 0, 0)

# Initialise the sound mixer
# Without this there can be a noticable
# delay when starting to .play a sound sample
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

canvas = pygame.display.set_mode((400, 690))

# Load the 'bounce' sound effect
bounce = pygame.mixer.Sound('assets/bounce.ogg')


class Brick(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        self.image = pygame.Surface((50, 30))
        self.image.fill(pygame.color.Color('brown'))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(location)


class Ball(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        self.image = pygame.Surface((30, 30), pygame.SRCALPHA)
        pygame.draw.circle(self.image, pygame.color.Color('blue'), (15, 15), 15)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(location)
        self.move_y = 10

    def update(self):
        self.rect.move_ip((0, self.move_y))
        if pygame.sprite.spritecollide(self, brick_spritegroup, False):
            self.move_y = -self.move_y

            # When the ball collides with a brick
            # play the 'bounce' sound effect
            bounce.play()


brick_spritegroup = pygame.sprite.Group()
ball_spritegroup = pygame.sprite.Group()

for i in range(6):
    brick_spritegroup.add(
        Brick((15 + 60 * i, 50 + 10 * i))
    )

    brick_spritegroup.add(
        Brick((15 + 60 * i, 500))
    )

    ball_spritegroup.add(
        Ball((25 + 60 * i, 300))
    )

clock = pygame.time.Clock()

done = False
while not done:

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            done = True

    canvas.fill(BLACK)
    brick_spritegroup.draw(canvas)
    ball_spritegroup.draw(canvas)
    pygame.display.flip()

    ball_spritegroup.update()
    clock.tick(30)
