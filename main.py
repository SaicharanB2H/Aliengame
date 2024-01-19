import pygame,sys

from settings import Settings #from file import class so that we can use its methods and attributes
from ship import Ship
import game_functions as gf
from pygame.sprite import *
from alien import Alien

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.ai_screen_width,ai_settings.ai_screen_height))
    pygame.display.set_caption("Charan Rocks")
    image_1 = pygame.image.load("Images/gmlogo.png")
    pygame.display.set_icon(image_1)
     
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings,screen)
    # Making a group to store bullets 
    bullets = Group()
    aliens = Group()

    # create a fleet of aliens
    gf.create_fleet(ai_settings,screen,ship,aliens)


    while True:


        # screen.fill(ai_settings.bg_color) #redraw the screen through the respective color every time
        # ship.blitme()
        gf.check_events(ai_settings, screen, ship, bullets) #taking all the events from game functions file 
        #The check events function is taking object as an input
        #updating the ship for movements 
        ship.update()
        

        gf.update_bullets(bullets)#update the bullets position and then remove the old bullets
        gf.update_aliens(aliens)

        gf.update_screen(ai_settings,screen,ship,aliens, bullets) #here the update screen is also taking the ai_settings and ship objects
        
        






       
run_game()