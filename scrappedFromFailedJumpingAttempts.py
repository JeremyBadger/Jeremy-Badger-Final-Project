'''A Testament to Failure'''

#if player.inJump == True:
#    onGround = False
#if player.rect.y >= 432:
#    pygame.quit()
#    sys.exit()
#if player.inJump == True:
#    if jumpheight == 5:
#        upDown = "DOWN"
#    elif jumpheight == 1:
#        upDown = "UP"
#    if upDown == "UP":
#        for x in range(jumpheight**2):
#            player.jump2(upDown, jumpheight)
#            for plat in plats:
#                plat_detect(player,plat,onGround)
#        jumpheight -= 1
#    else:
#        for x in range(jumpheight**2):
#            player.jump2(upDown, jumpheight)
#            for plat in plats:
#                plat_detect(player,plat, onGround)
#       jumpheight += 1

#if jumpheight == 10:
#    goingUp = False
#elif jumpheight == 5:
#    goingUp = True
#if goingUp:
#    for x in range(jumpheight ** 2) and not onGround:
#        player.jump3UP()
#        for plat in plats:
#            onGround = plat_detect(player, plat, onGround)
#    jumpheight += 1
#elif not goingUp:
#    for x in range(jumpheight ** 2) and not onGround:
#        player.jump3DOWN()
#        for plat in plats:
#            onGround = plat_detect(player, plat, onGround)
#    jumpheight -= 1
#if onGround == False and player.inJump == False:
#    for x in range(dropHeight ** 2):
#        player.rect.y += 1
#        for plat in plats:
#            plat_detect(player,plat, onGround)
#    dropHeight = (dropHeight+1)**2
#elif onGround == True and not player.inJump == True:
#    dropHeight = 1
#    player.inJump = False
#   upDown = "UP"

#if onGround == True:
    #jumpheight = 5
    #goingUp = True
    #for x in range(jumpheight ** 2):

#if player != "":
    #player.inJump = True
#    if onGround == True:
#        if player != "":
#            player.inJump = False

#onGround = True
#elif pygame.Rect.colliderect(entity1.rect, plat.left):
#    entity1.rect.x = plat.posX
#onGround = False
#elif pygame.Rect.colliderect(entity1.rect, plat.right):
#    entity1.rect.x = plat.posX + (plat.width * 50)
#onGround = False
#elif pygame.Rect.colliderect(entity1.rect, plat.bottom):
#b ,    entity1.rect.y = plat.posY + (plat.height * 50)
#onGround = False
#else:
#onGround = False
#return(onGround)

 #def jump2(self, upDown, height):
 #   if upDown == "UP":
  #      for x in range(height**2):
   #         self.rect.y -= 1
    #elif upDown == "DOWN":
     #   for x in range(height **2):
      #      self.rect.y += 1
#def jump3UP(self):
#    self.rect.y -= 1
#def jump3DOWN(self):
#        self.rect.y += 1
