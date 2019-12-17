"""
Playing sound effects in pygame

Sound level, repeat, fade in and out
"""


import time
import pygame

from utils import display_and_wait

# Initialise the sound mixer
# Without this there can be a noticable
# delay when starting to .play a sound sample
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

canvas = pygame.display.set_mode((400, 690))


# Load the sound samples
bounce = pygame.mixer.Sound('assets/bounce.ogg')
trampling = pygame.mixer.Sound('assets/trampling.ogg')
piano1 = pygame.mixer.Sound('assets/piano1.ogg')
piano2 = pygame.mixer.Sound('assets/piano2.ogg')


# Play the 'bounce' sound 5 times
bounce.play(5)

display_and_wait('Bounce x 5')

# Play both piano sounds indefinitely, or until stopped
piano1.play(-1)
piano2.play(-1)

display_and_wait('Piano 1 and 2, endless loop')

# Stop all sounds
pygame.mixer.stop()

# Set the volume for the 'piano1' sound to 20%
piano1.set_volume(0.2)
piano1.play(-1)
piano2.play(-1)

display_and_wait('Piano 1 and 2, with piano 1 on lower volume, on endless loop')
pygame.mixer.stop()

# Start 'piano1' at 0% sound volume
piano1.set_volume(0)
piano1.play(-1)

print('Piano 1, increasing in volume')
for i in range(70):
    # Increase the volume to 1%, 2%, ..., 70%
    piano1.set_volume(i / 100)
    time.sleep(0.1)

pygame.mixer.stop()
display_and_wait()


piano2.play(-1)
piano1.set_volume(0)
piano1.play(-1)
print('Piano 1 and 2, piano 1 increasing in volume')
for i in range(70):
    piano1.set_volume(i / 100)
    time.sleep(0.1)

pygame.mixer.stop()
display_and_wait()

print('Demonstrating .stop()')
piano1.play(-1)
piano2.play(-1)
time.sleep(2)

# Stop playing 'piano2' after 2 seconds
# This is a very abrupt stop
piano2.stop()
time.sleep(2)
piano1.stop()

display_and_wait()

print('Demonstrating .fadeout()')
piano1.play(-1)
piano2.play(-1)
time.sleep(2)

# Fade out 'piano2' after 2 seconds,
# over a period of 1000 milliseconds (1 second)
piano2.fadeout(1000)
time.sleep(2)

# Fade out 'piano1' another 2 seconds later
piano1.fadeout(500)

display_and_wait()

print('Demonstrating fade in')
# Fade in 'piano1' over 2000 milliseconds (2 seconds)
piano1.play(-1, fade_ms=2000)

display_and_wait()
pygame.mixer.stop()
