import pygame, sys, time, random
from pygame.locals import *
FPS = 90
WHITE = (255,255,255)
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((1000,500), 0, 32)
pygame.display.set_caption("Light")
SOLARIO = pygame.image.load('resources/SO_igs.png')
SOLARIO = pygame.transform.scale(SOLARIO,(96,96))
#pygame.mouse.set_cursor(*pygame.cursors.arrow)
cursor = pygame.cursors.compile(pygame.cursors.broken_x)
pygame.mouse.set_cursor(*cursor)

while True:
    #Fill in background
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(SOLARIO,(1,1))

    #Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
        #if event.type == KEYDOWN:
