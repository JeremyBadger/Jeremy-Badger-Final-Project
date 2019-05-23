import pygame, sys, time, random
from pygame.locals import *
FLAG = pygame.image.load('resources/flag.png')
FLAG = pygame.transform.scale(FLAG,(24,96))
class Win(pygame.sprite.Sprite):
    def __init__(self, x,y):

        #Creates the rect and image
        self.x = x
        self.y = y
        self.image = FLAG
        self.rect = pygame.Rect(self.x + 4,self.y,8,32)
    def isWin(self, player):

        #Checks if the game has been won, based on if the player is touching the flag
        win = False
        if pygame.Rect.colliderect(self.rect, player.rect):
            win = True
        return(win)
    def updateWin(self):

        #Sets the rect equal to the new x and y values, if they have changed due to the player reaching the edge of the screen
        self.rect = pygame.Rect(self.x + 4,self.y,8,32)
