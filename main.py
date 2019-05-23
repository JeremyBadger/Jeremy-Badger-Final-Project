import pygame, sys, time, random
from pygame.locals import *
from character import Character
from platform import Platform
from win import Win
#Sets up initial variables such as the FPS, backgrounds and colors
FPS = 15
pygame.init()
WHITE = (255,255,255)
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((768,432), 0, 32)
pygame.display.set_caption("Light")
ENTER = pygame.image.load('resources/Backgrounds/enterscene.png')
ENTER = pygame.transform.scale(ENTER,(768,432))
DAY1 = pygame.image.load('resources/Backgrounds/BetterDBG.png')
DAY1 = pygame.transform.scale(DAY1,(768,432))
NIGHT1 = pygame.image.load('resources/Backgrounds/BetterNBG.png')
NIGHT1 = pygame.transform.scale(NIGHT1,(768,432))
WINSCREEN = pygame.image.load('resources/Backgrounds/winscreen.png')
WINSCREEN = pygame.transform.scale(WINSCREEN,(768,432))
stage = "ENTER"
character = ""
player = ""
upDown = "UP"
jumpheight = 5
onGround = True
pygame.key.set_repeat(120,30)

#Creates the win object (flag), and all of the platforms needed for the stage
flag = Win(1725, 29)
grassp1 = Platform(10, 1, 0, 382, 'resources/Platform-Textures/plat-text-dirt.png')
grassp2 = Platform(2, 1, 500, 282, 'resources/Platform-Textures/plat-text-dirt.png')
grassp3 = Platform(2, 1, 675, 182, 'resources/Platform-Textures/plat-text-dirt.png')
grassp4 = Platform(4, 1, 850, 182, 'resources/Platform-Textures/plat-text-dirt.png')
grassp5 = Platform(1, 1, 1045, 100, 'resources/Platform-Textures/plat-text-dirt.png')
grassp6 = Platform(1, 1, 1245, 300, 'resources/Platform-Textures/plat-text-dirt.png')
grassp7 = Platform(1, 3, 1375, 200, 'resources/Platform-Textures/plat-text-dirt.png')
grassp8 = Platform(3, 1, 1375, 200, 'resources/Platform-Textures/plat-text-dirt.png')
grassp9 = Platform(2, 1, 1450, 370, 'resources/Platform-Textures/plat-text-dirt.png')
grassp10 = Platform(1, 1, 1725, 370, 'resources/Platform-Textures/plat-text-dirt.png')
grassp11 = Platform(5, 1, 1875, 250, 'resources/Platform-Textures/plat-text-dirt.png')
grassp12 = Platform(1, 1, 1725, 125, 'resources/Platform-Textures/plat-text-dirt.png')

#Adds all of the platforms to a sprite group to be utilized later
plats = pygame.sprite.Group()
plats.add(grassp1)
plats.add(grassp2)
plats.add(grassp3)
plats.add(grassp4)
plats.add(grassp5)
plats.add(grassp6)
plats.add(grassp7)
plats.add(grassp8)
plats.add(grassp9)
plats.add(grassp10)
plats.add(grassp11)
plats.add(grassp12)

#Sets the initial fromPlat to the first platform
fromPlat = grassp1

#Detects if the player is on top of a platform, or colliding with one of the sides
def plat_detect(entity1, plat, prevPlat):
    if pygame.Rect.colliderect(entity1.rect, plat.top) and not pygame.Rect.colliderect(entity1.rect, plat.left) and not pygame.Rect.colliderect(entity1.rect, plat.right) and not pygame.Rect.colliderect(entity1.rect, plat.bottom):

        #fromPlat is a variable used in the player's update function, which lets the program know how high the player can jump, based on the platform it came from
        fromPlat = plat
    elif pygame.Rect.colliderect(entity1.rect, plat.left):

        #For left, right, and bottom collisions, it places the player outside of the platform it was colliding with
        entity1.rect.x = plat.posX - 45
        fromPlat = prevPlat
    elif pygame.Rect.colliderect(entity1.rect, plat.right):
        entity1.rect.x = plat.posX + (plat.width * 50)
        fromPlat = prevPlat
    elif pygame.Rect.colliderect(entity1.rect, plat.bottom):
        entity1.rect.y = plat.posY + (plat.height * 50)

        #Sets the player to falling, a variable which is important in the player's update function
        player.fall = True
        fromPlat = prevPlat
    else:
        fromPlat = prevPlat
    return(fromPlat)

while True:

    #Fills in background, based on which stage of the game it is
    if stage == "ENTER":
        DISPLAYSURF.blit(ENTER,(0,0))

    #Once through the enterance, sets the theme to day. The initial plan was to create two characters, one night and one day themed.
    elif stage == "1-1":
        DISPLAYSURF.blit(DAY1,(0,0))
        DISPLAYSURF.blit(player.image, (player.rect.x, player.rect.y))
        posHolder = 0

        #Loops through the plats group to display each platform
        for plat in plats:

            #Makes the platforms appear not stretched by using a list of the platform's texture
            for x in plat.imagelist:
                DISPLAYSURF.blit(x,(plat.posX + posHolder,plat.posY))
                posHolder += 50
            posHolder = 0

        #Displays the player and win flag
        DISPLAYSURF.blit(player.image, (player.rect.x, player.rect.y))
        DISPLAYSURF.blit(flag.image, (flag.rect.x, flag.rect.y))

    #Displays the win stage if a victory is reached
    elif stage == "WIN":
        DISPLAYSURF.blit(WINSCREEN,(0,0))

    #Event loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Allows you to press enter to enter the game
        if event.type == KEYDOWN:
            if stage == "ENTER":
                if event.key == K_RETURN:
                    stage = "1-1"

                    #Character is named Solario because there was intended to be two characters, and the parameter for the name is still in existance
                    player = Character("SOLARIO")

            #Allows the character to run and jump when not in the entrance screen
            if stage != "ENTER":
                if event.key == K_a:
                    player.runL()
                elif event.key == K_d:
                    player.runR()
                if event.key == K_SPACE:
                    player.jump4()

        #Makes the player stop running when the key is released
        if event.type == KEYUP:
            if event.key == K_a:
                player.runningleft = False
            elif event.key == K_d:
                player.runningRight = False

    #The extremely important 'if player != "":', making things only happen if the player is actually a character object, rather than a string
    if player != "":

        #Moves the flag and platforms if the player has reached the edge of the screen, entering a new zone
        flag.updateWin()
        for x in plats:
            x.updatePlat()

            #Gets the platform that the player is coming from, and if the player is colliding with the sides or bottom
            fromPlat = plat_detect(player, x, fromPlat)

        #Sets the platform to the first platform if it is a NoneType, since this fixed errors and did not cause new bug
        if fromPlat == None:
            fromPlat = grassp1

        #Updates the player. Explained in character class
        fromPlat = player.update(plats, fromPlat)

        #Kills you if you fall out of the zone
        if player.rect.y >= 432:
            print("You died!")
            pygame.quit()
            sys.exit()

        #Pushes the platforms, player, and win flag to the left or right if the player reaches near the edge of the screen
        if player.rect.x >= 700:
            for p in plats:
                p.posX -= 632
            player.rect.x -= 632
            flag.x -= 632
        elif player.rect.x <= 68:
            for p in plats:
                p.posX += 632
            player.rect.x += 632
            flag.x += 632

        #Determines if the player has won
        win = flag.isWin(player)
        if win:
            stage = "WIN"
    pygame.display.update()
    fpsClock.tick(FPS)
