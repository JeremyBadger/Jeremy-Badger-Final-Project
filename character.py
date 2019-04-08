import pygame, sys, time, random
from pygame.locals import *
class Character(self):
    def __init__(self, name):
        self.name = name
        self.def = 0
        self.att = 0
        self.hp = 100
        self.light = 15
        self.theme = ""
        if self.name == "SOLARIO":
            self.att = 2
            self.hp = 125
            self.theme = "LIGHT"
        elif self.name == "LUNA":
            self.att = 1
            self.light = 25
            self.theme = "NIGHT"
    
