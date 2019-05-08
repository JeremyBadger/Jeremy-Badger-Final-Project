import pygame, sys, time, random
from pygame.locals import *
DIRT = pygame.image.load('resources/Platform-Textures/plat-text-dirt.png')
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, texture):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, 50,50*height)
        bottom = Rect(posX, posY + 49, width * 50, 1)
        top = Rect(posX, posY, width*50, 1)
        left = Rect(posX, posY + 3, 1, 47)
        right = Rect(posX + (width * 50), posY + 3, 1, 47 )
