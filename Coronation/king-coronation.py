import pygame
from math import *

clock = pygame.time.Clock()

WIDTH = 1200

HEIGHT = 600

pygame.display.set_caption("King's Coronation By @SmashedFrenzy16")

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

picture = pygame.image.load("coron_pic.png").convert()

scrolling = 0

tiles = ceil(WIDTH / picture.get_width()) + 1

while 1:

    clock.tick(60)

    i = 0

    while 1 < tiles:

        SCREEN.blit(picture, (picture.get_width() * i + scrolling, 0))

        scrolling = -6

        if abs(scrolling) > picture.get_width():

            scrolling = 0

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                quit()

        pygame.display.update()

pygame.quit()