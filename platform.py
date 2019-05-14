import pygame, sys, time, random
from pygame.locals import *
DIRT = pygame.image.load('resources/Platform-Textures/plat-text-dirt.png')
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, texture):
        super().__init__()
        self.texture = pygame.image.load(texture)
        #self.texture = pygame.transform.scale(self.texture, (50* width,50*height))
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.imagelist = []
        for x in range(self.width):
            self.imagelist.append(self.texture)
        self.bottom = pygame.Rect(self.posX, self.posY + 49, self.width * 50, 10)
        self.top = pygame.Rect(self.posX, self.posY, self.width*50, 10)
        self.left = pygame.Rect(self.posX, self.posY + 3, 1, 47)
        self.right = pygame.Rect(self.posX + (self.width * 50), self.posY + 3, 1, 47 )
