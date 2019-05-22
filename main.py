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
jumpheight = 5
onGround = False
global dropHeight
dropHeight = 1
pygame.key.set_repeat(120,30)
def plat_detect(entity1, plat, onGround):
    if pygame.Rect.colliderect(entity1.rect, plat.top):
        entity1.rect.y = plat.posY - 90
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
                    if onGround == True:
                        player.jump4():
                        player.update(plats):
                        #for x in range(jumpheight ** 2):
                        #    player.jump2(upDown,jumpheight)

                        #player.inJump = True
                        #print("jump")
    if onGround == True:
        player.inJump = False

    if player != "":
        if player.inJump == True:
            onGround = False
        if player.rect.y >= 432:
            pygame.quit()
            sys.exit()
        if player.inJump == True:
            player.update
            #if jumpheight == 90:
            #    upDown = "DOWN"
            #elif jumpheight == 1:
            #    upDown = "UP"
            #if upDown == "UP":
            #    for x in range(jumpheight**2):
            #        player.jump2(upDown, jumpheight, onGround)
            #        for plat in plats:
            #            plat_detect(player,plat)
            #    jumpheight -= 1
            #else:
            #    for x in range(jumpheight**2):
            #        player.jump2(upDown, jumpheight)
            #        for plat in plats:
            #            plat_detect(player,plat, onGround)
            #    jumpheight += 1
        for x in plats:
            onGround = plat_detect(player, x, onGround)
        if onGround == False and player.inJump == False:
            for x in range(dropHeight ** 2):
                player.rect.y += 1
                for plat in plats:
                    plat_detect(player,plat, onGround)
            dropHeight = (dropHeight+1)**2
        elif onGround == True and not player.inJump == True:
            dropHeight = 1
            player.inJump = False
            upDown = "UP"
    pygame.display.update()
    fpsClock.tick(FPS)
