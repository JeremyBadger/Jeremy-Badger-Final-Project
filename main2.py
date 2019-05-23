import pygame, sys, time, random
from pygame.locals import *
from character import Character
from platform import Platform
#Test
FPS = 7
pygame.init()
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
grassp1 = Platform(10, 1, 0, 382, 'resources/Platform-Textures/plat-text-dirt.png')
stage = "SELECT"
character = ""
player = ""
plats = pygame.sprite.Group()
plats.add(grassp1)
upDown = "UP"
fromPlat = ""
jumpheight = 5
onGround = True
pygame.key.set_repeat(120,30)
def plat_detect(entity1, plat, fromPlat):
    if pygame.Rect.colliderect(entity1.rect, plat.top):
        #if not entity1.inJump and not onGround:
        entity1.rect.y = plat.posY - 90
        fromPlat = plat
    return(fromPlat)

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
        DISPLAYSURF.blit(player.image, (player.rect.x, player.rect.y))
        posHolder = 0
        for plat in plats:
            for x in plat.imagelist:
                DISPLAYSURF.blit(x,(plat.posX + posHolder,plat.posY))
                posHolder += 50
        DISPLAYSURF.blit(player.image, (player.rect.x, player.rect.y))

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
            if stage != "SELECT":
                if event.key == K_a:
                    player.rect.x -= 10
                elif event.key == K_d:
                    player.rect.x += 10
                if event.key == K_SPACE:
                    player.jump4()
    if player != "":
        for x in plats:
            fromPlat = plat_detect(player, x, fromPlat)
        player.update(plats, fromPlat)
    pygame.display.update()
    fpsClock.tick(FPS)
