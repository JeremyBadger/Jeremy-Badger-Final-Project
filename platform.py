import pygame, sys, time, random
from pygame.locals import *
DIRT = pygame.image.load('resources/Platform-Textures/plat-text-dirt.png')
class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, posX, posY, texture):
        super().__init__()

        #Sets up basic variables
        self.texture = pygame.image.load(texture)
        self.texture = pygame.transform.scale(self.texture, (50,50*height))
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height

        #Makes a list of images to know how many times to draw the texture, so that it is not stretched out
        self.imagelist = []
        for x in range(self.width):
            self.imagelist.append(self.texture)

        #Creates all four platform rects
        self.bottom = pygame.Rect(self.posX, self.posY + 49, self.width * 50, 10)
        self.top = pygame.Rect(self.posX, self.posY, self.width*50, 10)
        self.left = pygame.Rect(self.posX, self.posY + 3, 1, 4)
        self.right = pygame.Rect(self.posX + (self.width * 50), self.posY + 3, 1, 4 )
    def updatePlat(self):

        #Sets the rects to the new x and y coordinates if the player moves to either edge of the screen 
        self.bottom = pygame.Rect(self.posX, self.posY + 49, self.width * 50, 10)
        self.top = pygame.Rect(self.posX, self.posY, self.width*50, 10)
        self.left = pygame.Rect(self.posX, self.posY + 3, 1, 4)
        self.right = pygame.Rect(self.posX + (self.width * 50), self.posY + 3, 1, 4 )
