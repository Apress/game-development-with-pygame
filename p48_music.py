"""
Playing music in pygame
"""


import time
import pygame

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()

print('=' * 20)

# Music sample from https://freepd.com/upbeat.php,
# originally called Ukekele Song, converted to .ogg
# and renamed to music.ogg for this demonstration

# Start loading the music file
pygame.mixer.music.load('assets/music.ogg')

# Start streaming the music file
pygame.mixer.music.play()
print('start playing')

time.sleep(2)

# Change the volume to 20%
pygame.mixer.music.set_volume(0.2)
print('volume set to 0.2')

time.sleep(2)

# Pause streaming the music
pygame.mixer.music.pause()
print('music paused')

time.sleep(2)

# Continue streaming the music
pygame.mixer.music.unpause()
print('music unpaused')

# Wait 5 seconds
time.sleep(5)

print('done')

# Exit the program
# This will also stop streaming the music
