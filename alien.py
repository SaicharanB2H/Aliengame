import pygame 
from pygame.sprite import  Sprite

class Alien(Sprite):
    ''' A class to represent a single alien in the fleet '''
    def __init__(self, ai_settings, screen) -> None:
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #load the images and set it rect attributes
        self.image = pygame.image.load("Images/alien1.bmp")
        self.rect = self.image.get_rect() #Treating the image as rectangle 

        #start each new alien near the top left corner of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store the aliens exact position
        self.x = float(self.rect.x)

    def blitme(self):
        ''' Draw the alien on the screen '''
        self.screen.blit(self.image, self.rect)
        # print(f'The x-coordinate of the ship is {self.rect.x}')
        # print(f'The y-coordinate of the ship is {self.rect.y}')

    def update(self):
        ''' move aliens to right '''
        self.x += self.ai_settings.alien_speed_factor
        self.rect.x = self.x
        