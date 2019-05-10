import pygame, sys, time, random
from pygame.locals import *
from character import Character
from platform import Platform
FPS = 90
WHITE = (255,255,255)
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((768,432), 0, 32)
pygame.display.set_caption("Light")
SELECT = pygame.image.load('resources/Backgrounds/chSel.png')
SELECT = pygame.transform.scale(SELECT,(768,432))
DAY1 = pygame.image.load('resources/Backgrounds/BetterDBG.png')
DAY1 = pygame.transform.scale(DAY1,(768,432))
NIGHT1 = pygame.image.load('resources/Backgrounds/BetterNBG.png')
NIGHT1 = pygame.transform.scale(NIGHT1,(768,432))
soSelect = pygame.Rect(129, 147, 222, 237)
grassp1 = Platform(10, 1, 0, 382, 'resources/Platform-Textures/plat-text-dirt.png')
stage = "SELECT"
character = ""
player = ""
def plat_detect(entity1, plat):
    if pygame.sprite.spritecollideany(entity1, plat.top):
        entity1.rect.y = plat.posY - 96
    elif pygame.sprite.spritecollideany(entity1, plat.left):
        entity1.rect.x = plat.posX
    elif pygame.sprite.spritecollideany(entity1, plat.right):
        entity1.rect.x = plat.posX + (plat.width * 50)
    elif pygame.sprite.spritecollideany(entity1, plat.bottom):
        entity1.rect.y = plat.posY + (plat.height * 50)

while True:
    #Fill in background
    DISPLAYSURF.fill(WHITE)
    if stage == "SELECT":
        DISPLAYSURF.blit(SELECT,(1,1))
    elif stage == "1-1":
        if player.name == "SOLARIO":
            DISPLAYSURF.blit(DAY1,(1,1))
        elif player.name == "LUNA":
            DISPLAYSURF.blit(NIGHT1,(1,1))
    if player != "":
        DISPLAYSURF.blit(player.image, (player.x, player.y))
        DISPLAYSURF.blit(grassp1.texture,(grassp1.posX,grassp1.posY))

    #Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if stage == "SELECT":
                if event.key == K_LEFT:
                    character = "SOLARIO"
                elif event.key == K_RIGHT:
                    character = "LUNA"
                if character != "" and event.key == K_RETURN:
                    stage = "1-1"
                    player = Character(character)
    pygame.display.update()
