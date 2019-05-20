import pygame, sys, time, random
from pygame.locals import *
from character import Character
from platform import Platform
#Test
FPS = 90
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
soSelect = pygame.Rect(129, 147, 222, 237)
grassp1 = Platform(10, 1, 0, 382, 'resources/Platform-Textures/plat-text-dirt.png')
stage = "SELECT"
character = ""
player = ""
plats = pygame.sprite.Group()
plats.add(grassp1)
onGround = True
global dropHeight
dropHeight = 1
pygame.key.set_repeat(120,30)
def plat_detect(entity1, plat, onGround):
    if pygame.Rect.colliderect(entity1.rect, plat.top):
        if player.inJump == False:
            entity1.rect.y = plat.posY - 96
        onGround = True
    elif pygame.Rect.colliderect(entity1.rect, plat.left):
        entity1.rect.x = plat.posX
        onGround = False
    elif pygame.Rect.colliderect(entity1.rect, plat.right):
        entity1.rect.x = plat.posX + (plat.width * 50)
        onGround = False
    elif pygame.Rect.colliderect(entity1.rect, plat.bottom):
        entity1.rect.y = plat.posY + (plat.height * 50)
        onGround = False
    else:
        onGround = False
    return(onGround)

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
        for x in grassp1.imagelist:
            DISPLAYSURF.blit(x,(grassp1.posX + posHolder,grassp1.posY))
            posHolder += 50

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
                    if onGround == True:
                        player.jump()
    #if onGround == False:

    if player != "":
        for x in plats:
            if player.inJump == False:
                onGround = plat_detect(player, x, onGround)
        if onGround == False and player.inJump == False:
            player.rect.y += dropHeight
            dropHeight += dropHeight**2
        else:
            dropHeight = .1
            player.UOrD = 0
            player.heightNum = 2
            player.inJump = False
        if player.inJump == True:
            if player.heightNum == 13:
                player.UOrD = 1
                player.jump()
            elif player.heightNum != 13 and player.heightNum != 2:
                player.jump()
    pygame.display.update()
