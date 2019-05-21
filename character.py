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
        self.defense = 0
        self.att = 0
        self.hp = 100
        self.light = 15
        self.rect = pygame.Rect(self.x,self.y,54,96)
        self.heightNum = 2
        self.UOrD = 0
        self.inJump = False
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
    def jump2(self, upDown, jumpheight):
        if upDown == "UP":
            self.rect.y -= 1
        elif upDown == "DOWN":
            self.rect.y += 1
