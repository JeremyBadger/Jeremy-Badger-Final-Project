import pygame, sys, time, random
from pygame.locals import *
from character import Character
from platform import Platform
#Test
FPS = 15
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
grassp2 = Platform(2, 1, 500, 282, 'resources/Platform-Textures/plat-text-dirt.png')
stage = "SELECT"
character = ""
player = ""
plats = pygame.sprite.Group()
plats.add(grassp1)
plats.add(grassp2)
upDown = "UP"
fromPlat = grassp1
jumpheight = 5
onGround = True
pygame.key.set_repeat(120,30)
def plat_detect(entity1, plat, fromPlat):
    if pygame.Rect.colliderect(entity1.rect, plat.top) and not pygame.Rect.colliderect(entity1.rect, plat.left) and not pygame.Rect.colliderect(entity1.rect, plat.right) and not pygame.Rect.colliderect(entity1.rect, plat.bottom):
        fromPlat = plat
    elif pygame.Rect.colliderect(entity1.rect, plat.left):
        entity1.rect.x = plat.posX - 45
    elif pygame.Rect.colliderect(entity1.rect, plat.right):
        entity1.rect.x = plat.posX + (plat.width * 50)
    elif pygame.Rect.colliderect(entity1.rect, plat.bottom):
        entity1.rect.y = plat.posY + (plat.height * 50)
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
            posHolder = 0
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
                    player.runL()
                elif event.key == K_d:
                    player.runR()
                if event.key == K_SPACE:
                    player.jump4()
        if event.type == KEYUP:
            if event.key == K_a:
                player.runningleft = False
            elif event.key == K_d:
                player.runningRight = False
    if player != "":
        for x in plats:
            fromPlat = plat_detect(player, x, fromPlat)
        if fromPlat != "":
            fromPlat = player.update(plats, fromPlat)
        if player.rect.y >= 432:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
