import pygame
#one good thing about pygame is it let you treat game elements as rectangles
class Ship():
    def __init__(self,ai_settings,screen) -> None:
        self.screen = screen #this is the input taken by the class we create an object of this class 
        self.ai_settings = ai_settings

        #load the ship image and get its rect 
        self.image = pygame.image.load("images/ship.bmp") #this function returns a surface which represents a ship
        self.rect = self.image.get_rect()  #treating the loaded image as rectangle
        self.screen_rect = screen.get_rect()

        #starting the new ship at bottom center of the screen
        #settings the coordinates of the ship
        self.rect.centerx = self.screen_rect.centerx #matching the x-cordinate of ship with the screen
        self.rect.bottom = self.screen_rect.bottom #matching the y-coordinate of the ship with the screen

        #store decimal value of ship center 
        self.center = float(self.rect.centerx)
        #Movement flag
        self.moving_right = False
        self.moving_left = False


    def update(self):
        # "moving the ship based on the flag"
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.center += self.ai_settings.ship_speed_factor

        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect to the center location
        self.rect.centerx = self.center



    def blitme(self): 
        #drawing the ship on the screen blit take two arguments blit(loaded image,rectagular cordinates)
        self.screen.blit(self.image, self.rect)   #now this self.rect gives both x and y cordinate of ship to the blit method