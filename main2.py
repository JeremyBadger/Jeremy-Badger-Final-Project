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
global dropHeight
dropHeight = 1
pygame.key.set_repeat(120,30)
def plat_detect(entity1, plat, fromPlat):
    if pygame.Rect.colliderect(entity1.rect, plat.top):
        #if not entity1.inJump and not onGround:
        entity1.rect.y = plat.posY - 90
        fromPlat = plat
            #onGround = True
    #elif pygame.Rect.colliderect(entity1.rect, plat.left):
    #    entity1.rect.x = plat.posX
        #onGround = False
    #elif pygame.Rect.colliderect(entity1.rect, plat.right):
    #    entity1.rect.x = plat.posX + (plat.width * 50)
        #onGround = False
    #elif pygame.Rect.colliderect(entity1.rect, plat.bottom):
    #b ,    entity1.rect.y = plat.posY + (plat.height * 50)
        #onGround = False
    #else:
        #onGround = False
    #return(onGround)
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
                    #if onGround == True:
                        #jumpheight = 5
                        #goingUp = True
                        #for x in range(jumpheight ** 2):
                    player.jump4()
                        #if player != "":
                            #player.inJump = True
#    if onGround == True:
#        if player != "":
#            player.inJump = False

    if player != "":
        #if player.inJump == True:
        #    onGround = False
        if player.rect.y >= 432:
            pygame.quit()
            sys.exit()
    #if player.inJump == True:
        #    if jumpheight == 5:
        #        upDown = "DOWN"
        #    elif jumpheight == 1:
        #        upDown = "UP"
        #    if upDown == "UP":
        #        for x in range(jumpheight**2):
        #            player.jump2(upDown, jumpheight)
        #            for plat in plats:
        #                plat_detect(player,plat,onGround)
        #        jumpheight -= 1
        #    else:
        #        for x in range(jumpheight**2):
        #            player.jump2(upDown, jumpheight)
        #            for plat in plats:
        #                plat_detect(player,plat, onGround)
        #       jumpheight += 1
        for x in plats:
            fromPlat = plat_detect(player, x, fromPlat)
        player.update(plats, fromPlat)
            #if jumpheight == 10:
            #    goingUp = False
            #elif jumpheight == 5:
            #    goingUp = True
            #if goingUp:
            #    for x in range(jumpheight ** 2) and not onGround:
            #        player.jump3UP()
            #        for plat in plats:
            #            onGround = plat_detect(player, plat, onGround)
            #    jumpheight += 1
            #elif not goingUp:
            #    for x in range(jumpheight ** 2) and not onGround:
            #        player.jump3DOWN()
            #        for plat in plats:
            #            onGround = plat_detect(player, plat, onGround)
            #    jumpheight -= 1
    #if onGround == False and player.inJump == False:
        #    for x in range(dropHeight ** 2):
        #        player.rect.y += 1
        #        for plat in plats:
        #            plat_detect(player,plat, onGround)
        #    dropHeight = (dropHeight+1)**2
        #elif onGround == True and not player.inJump == True:
        #    dropHeight = 1
        #    player.inJump = False
        #   upDown = "UP"
    pygame.display.update()
    fpsClock.tick(FPS)
