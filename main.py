import pygame, sys, time, random
from pygame.locals import *
FPS = 90
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("Dino Jump")


while True:
    #Fill in background
    DISPLAYSURF.fill(WHITE)

    #Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
