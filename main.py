import pygame, sys, time, random
from pygame.locals import *
FPS = 90
WHITE = (255,255,255)
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((768,432), 0, 32)
pygame.display.set_caption("Light")
SOLARIO = pygame.image.load('resources/SO_igs.png')
SOLARIO = pygame.transform.scale(SOLARIO,(96,96))
SELECT = pygame.image.load('resources/chSel.png')
SELECT = pygame.transform.scale(SELECT,(768,432))
soSelect = pygame.Rect(129, 147, 222, 237)
mouse = pygame.Rect(1,1, 5,5)
mousepos = pygame.mouse.get_pos()


while True:
    #Fill in background
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(SELECT,(1,1))
    if sprite.collideany(mouse,soSelect):
        DISPLAYSURF.blit(SOLARIO,(1,1))

    #Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
        #if event.type == KEYDOWN:
