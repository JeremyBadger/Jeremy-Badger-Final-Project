import pygame, sys, time, random
from pygame.locals import *
class Character(pygame.sprite.Sprite):
    def __init__(self, name):
        self.name = name
        self.defense = 0
        self.att = 0
        self.hp = 100
        self.light = 15
        global theme
        if self.name == "SOLARIO":
            self.att = 2
            self.hp = 125
            theme = "LIGHT"
        elif self.name == "LUNA":
            self.att = 1
            self.light = 25
            theme = "NIGHT"
