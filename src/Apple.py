import pygame
import random
from src.Config import Config

class Apple:
    def __init__(self,display):
        self.display = display
        self.x_pos = 0
        self.y_pos = 0
        self.randomize()

    def randomize(self):
        height = Config['game']['height']
        width  = Config['game']['width']
        bumper = Config['game']['bumper_size']

        max_x = (height - bumper - Config['snake']['width'])
        max_y = (width - bumper - Config['snake']['height'])

        self.x_pos = random.randint(bumper,max_x)
        self.y_pos = random.randint(bumper,max_y)
    
    def draw(self):
        #print(self.x_pos,self.y_pos)
        return pygame.draw.rect(self.display,Config['colors']['bright_red'],[ 
            self.x_pos,self.y_pos,Config['apple']['height'],Config['apple']['width']
        ])