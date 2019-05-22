import pygame, sys, time, random
from pygame.locals import *
SOLARIO = pygame.image.load('resources/CharEnemy/SO_igs.png')
SOLARIO = pygame.transform.scale(SOLARIO,(96,96))
class Character(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.x = 0
        self.y = 432-96
        #self.defense = 0
        #self.att = 0
        #self.hp = 100
        #self.light = 15
        self.rect = pygame.Rect(self.x,self.y,54,96)
        #self.heightNum = 2
        #self.UOrD = 0
        self.v = 8
        self.m = 10
        self.F = 0
        self.inJump = False
        self.goingUp = True
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
     #def jump2(self, upDown, height):
     #   if upDown == "UP":
      #      for x in range(height**2):
       #         self.rect.y -= 1
        #elif upDown == "DOWN":
         #   for x in range(height **2):
          #      self.rect.y += 1
    #def jump3UP(self):
    #    self.rect.y -= 1
    #def jump3DOWN(self):
#        self.rect.y += 1

    #yes this is my FOURTH attempt in the last three days to get the &%*$*@# jump to work
    #Shamelessly stolen from pythonspot.com because I have already put ~10 hrs into the jump command, probably wont work anyway...
    def jump4(self):
        self.inJump = True
    def update(self, plats, fromPlat):
        if self.inJump:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if fromPlat != "":
                F = ( 0.5 * self.m * (self.v*self.v) )
                #else:
                #    F = -( 0.5 * self.m * (self.v*self.v) )

                if self.rect.y > fromPlat.top.y - 150:
                    # Change position
                    for s in range(round(F)) and self.rect.y :
                        self.rect.y = self.rect.y - 1
                else:
                    for s in range(round(F)):
                        self.rect.y += 1

                # Change velocity
                self.v = self.v - 1

                # If ground is reached, reset variables.
                for plat in plats:
                    if plat != "":
                        if self.rect.y == plat.top.y - 96:
                            self.rect.y = plat.top.y - 96
                            self.isjump = False
                            self.v = 8
                            self.goingUp = True
