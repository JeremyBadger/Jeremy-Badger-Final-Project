import pygame, sys, time, random
from pygame.locals import *
DIRT = pygame.image.load('resources/Platform-Textures/plat-text-dirt.png')
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, hight, posX, posY, texture):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, 50,50)
        
