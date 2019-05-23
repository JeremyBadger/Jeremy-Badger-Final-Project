import pygame, sys, time, random
from pygame.locals import *
from platform import Platform
SOLARIO = pygame.image.load('resources/CharEnemy/SO_igs.png')
SOLARIO = pygame.transform.scale(SOLARIO,(96,96))
class Character(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()

        #Sets up the character's rect, velocity, mass, and variables regarding if the character is jumping, falling, or running
        self.name = name
        self.x = 70
        self.y = 280
        self.rect = pygame.Rect(self.x,self.y,54,96)
        self.v = 10
        self.m = 1
        self.inJump = False
        self.fall = False
        self.runningleft = False
        self.runningRight = False

        #Remnants of the theme and two-character system that was later scrapped
        global theme
        if self.name == "SOLARIO":
            self.att = 2
            self.hp = 125
            theme = "LIGHT"
            self.image = SOLARIO
        elif self.name == "LUNA":
            self.att = 1
            self.light = 25
            theme = "NIGHT"

    #When the 'a' or 'd' key is pressed, makes the variable regarding the direction of running true
    def runR(self):
        self.runningRight = True
    def runL(self):
        self.runningleft = True

    #Named jump4 because of my fourth attempt to entirely rewrite the jump command
    def jump4(self):
        self.inJump = True
    def update(self, plats, prevPlat):

        #Loops through the plats group to see if the character is not on any platforms while not jumping. If so, the player falls
        notOn = 0
        fromPlat = prevPlat
        if not self.inJump:
            for plat in plats:
                if not pygame.Rect.colliderect(self.rect, plat.top):
                    notOn += 1
            if notOn == len(plats):
                self.inJump = True
                self.fall = True

        #Moves the character in the desired direction if told to move
        if self.runningleft:
            self.rect.x -= 20
        elif self.runningRight:
            self.rect.x += 20

        #If the player is jumping...
        if self.inJump:

            # Calculates the force, which I use as amount of loops through to increase/decrease height while checking for platform collision
            F = ( 0.5 * self.m * (self.v*self.v) )
            if self.fall == False:

                # Change position while not touching a platform
                s = 1
                while s in range(round(F)) and not self.fall:
                    self.rect.y = self.rect.y - 1
                    s += 1

                    #Makes sure the player does not go too high
                    if self.rect.y < fromPlat.top.y - 240:
                        self.fall = True
            else:
                s = 1
                for k in range(round(F)):
                    for newp in plats:

                        #When going down, resets variables if touching a new platform
                        if pygame.Rect.colliderect(self.rect, newp.top) and not pygame.Rect.colliderect(self.rect, newp.left) and not pygame.Rect.colliderect(self.rect, newp.right) and not pygame.Rect.colliderect(self.rect, newp.bottom):
                            self.fall = False
                            self.inJump = False
                            self.v = 10
                            self.rect.y = newp.top.y - 96
                            if type(newp) == Platform:
                                fromPlat = newp

                    #If the player did not hit a platform, continues to go down
                    if self.fall:
                        self.rect.y += 1
            self.v = self.v - .1
            return(fromPlat)
