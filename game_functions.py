import sys, pygame
from bullet import Bullet
from alien import Alien

def fire_bullets(ai_settings,screen, ship, bullets):
    #create a new bullet and add it to group
    if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def get_number_rows(ai_settings,ship_height, alien_height):
    '''Determines the no of rows of aliens that can fit in the screen '''
    availspace_y = ai_settings.ai_screen_height - (3*alien_height) - ship_height
    number_rows = int(availspace_y / (2*alien_height))
    return number_rows

def update_aliens(aliens):
    ''' update the position of the whole fleet '''
    aliens.update()



def get_number_aliens_x(ai_settings,alien_width):
    '''This function determines the no of aliens that can fit in the screen'''
    avaiable_space_x = ai_settings.ai_screen_width - 2*alien_width
    number_aliens_x = int(avaiable_space_x/(2*alien_width))
    return number_aliens_x

def create_alien(ai_settings,screen,aliens,alien_number, row_number):
    alien = Alien(ai_settings,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_number*alien_width
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2*alien.rect.height *row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen ,ship,aliens):
    ''' Create full fleet of aliens'''
    alien = Alien(ai_settings,screen)
    number_aliens_x = get_number_aliens_x(ai_settings,alien.rect.width)
    number_rows = get_number_rows(ai_settings,ship.rect.height,alien.rect.height)

    #creating the fleet of aliens
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_number,row_number)



def check_keydown_events(event,ai_settings,screen,ship,bullets):
    #Respond to Key presses
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullets(ai_settings,screen,ship,bullets)
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event,ship):
    #Respond to key releases
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False





def check_events(ai_settings, screen, ship, bullets):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN: #Detecting the key down event 
            check_keydown_events(event,ai_settings,screen,ship,bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)





def update_screen(ai_settings,screen, ship,alien,bullets):
    screen.fill(ai_settings.bg_color)
    #redraw all bullets behind the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()
    alien.draw(screen)

    pygame.display.flip()


def update_bullets(bullets):
    ''' update the position of bullets and then get rid of the old bullets '''
    bullets.update()
    #getting rid of bullets
    for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        