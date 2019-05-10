import pygame, sys, time, random
from pygame.locals import *
DIRT = pygame.image.load('resources/Platform-Textures/plat-text-dirt.png')
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, texture):
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (50* width,50*height))
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        bottom = Rect(self.posX, self.posY + 49, self.width * 50, 1)
        top = Rect(self.posX, self.posY, self.width*50, 1)
        left = Rect(self.posX, self.posY + 3, 1, 47)
        right = Rect(self.posX + (self.width * 50), self.posY + 3, 1, 47 )
