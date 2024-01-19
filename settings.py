class Settings():
    def __init__(self) -> None:
        self.ai_screen_width = 1200
        self.ai_screen_height = 800
        self.bg_color = (230,230,230)

        #ship speed 
        self.ship_speed_factor = 1.5

        #Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        #Fleet direction 1--> right & -1 --> left
        self.fleet_direction = 1

        #Bullet settings i.e a small rectangle 
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 80, 60, 60
        self.bullets_allowed = 3