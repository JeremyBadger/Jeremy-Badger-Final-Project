import pygame, sys, time, random
from pygame.locals import *
SOLARIO = pygame.image.load('resources/CharEnemy/SO_igs.png')
SOLARIO = pygame.transform.scale(SOLARIO,(96,96))
class Character(pygame.sprite.Sprite):
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 300
        self.defense = 0
        self.att = 0
        self.hp = 100
        self.light = 15
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
