import pygame
from pygame.sprite import  Sprite

class Bullet(Sprite):
    #A class that manages bullets fired from the ship 
    def __init__(self,ai_settings, screen, ship) -> None:  #This bullet by defalut takes three objects 
        # create bullet object at the position of the ship always
        super(Bullet,self).__init__()  #super() function helps to inherit all methods from the parent class 
        #here the parent class is Sprite and bullet is the child class 
        self.screen = screen


        #create rect object at (0,0) and then set the current position 
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        '''Creating a rectangular bullet from the scratch 
        This Rect() function take x and y coordinate of the bullet object we create 
        And then set its position to position of the ship '''
        self.rect.centerx = ship.rect.centerx # making the x-coordinate of ship and bullet the same 
        self.rect.top = ship.rect.top  #bullet should emerge from the top of the ship 

    # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor


    def update(self):
        ''' Moving the bullet up the screen '''
        #update the decimal position of the bullet 
        self.y -= self.speed_factor

        #now update the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen """
        pygame.draw.rect(self.screen, self.color,self.rect)  
        ''' Syntax of pygame.draw.rect(surface , color, rect)
        surface on which we want to draw the object , color of the object , what we want to draw 
        rect- we created a rectangular object in the 14 th line '''
        