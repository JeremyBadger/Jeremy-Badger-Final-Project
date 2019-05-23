import pygame, sys, time, random
from pygame.locals import *
SOLARIO = pygame.image.load('resources/CharEnemy/SO_igs.png')
SOLARIO = pygame.transform.scale(SOLARIO,(96,96))
class Character(pygame.sprite.Sprite):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.x = 0
        self.y = 0
        self.rect = pygame.Rect(self.x,self.y,54,96)
        self.v = 10
        self.m = 1
        self.inJump = False
        self.goingUp = True
        self.fall = False
        self.runningleft = False
        self.runningRight = False
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
    def runR(self):
        self.runningRight = True
    def runL(self):
        self.runningleft = True
    def jump4(self):
        self.inJump = True
    def update(self, plats, fromPlat):
        notOn = 0
        if not self.inJump:
            for plat in plats:
                if not pygame.Rect.colliderect(self.rect, plat.top):
                    notOn += 1
            if notOn == len(plats):
                self.inJump = True
                self.fall = True
        if self.runningleft:
            self.rect.x -= 20
        elif self.runningRight:
            self.rect.x += 20
        if self.inJump:
            # Calculate force (F). F = 0.5 * mass * velocity^2.
            if fromPlat != "":
                F = ( 0.5 * self.m * (self.v*self.v) )

                if self.fall == False:
                    # Change position
                    s = 1
                    while s in range(round(F)) and not self.fall:
                        self.rect.y = self.rect.y - 1
                        s += 1
                        if self.rect.y < fromPlat.top.y - 240:
                            self.fall = True
                else:
                    s = 1
                    for k in range(round(F)):
                        for p in plats:
                            if pygame.Rect.colliderect(self.rect, p.top)  and not pygame.Rect.colliderect(self.rect, p.left) and not pygame.Rect.colliderect(self.rect, p.right) and not pygame.Rect.colliderect(self.rect, p.bottom):
                                self.fall = False
                                self.inJump = False
                                self.v = 10
                                self.rect.y = p.top.y - 96
                                fromPlat = p
                        if self.fall:
                            self.rect.y += 1
                self.v = self.v - .1
