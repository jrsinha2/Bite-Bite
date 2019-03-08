'''Sources: for pygame.draw.rect() https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect '''
import pygame

from src.Config import Config


class Snake:
    def __init__(self,display):
        self.x_pos = Config['game']['width']/2      #start ar middle of screen
        self.y_pos = Config['game']['height']/2
        self.display = display
        self.body = []
        self.max_size = 0
    def eat(self):
        self.max_size += 1
    def draw_body(self):
        for item in self.body:
            pygame.draw.rect(
                self.display,Config['colors']['green'],[
                    item[0],item[1],Config['snake']['height'],Config['snake']['width']
                ]
            )
    
    def draw(self):
        self.draw_body()
        return pygame.draw.rect(self.display, Config['colors']['green'],
        [ self.x_pos,self.y_pos,Config['snake']['height'],Config['snake']['width']
        ] ) #rect(Surface,color,Rect,width = 0) #filled rectangle
    
    def move(self,dx,dy):
        self.body.append((self.x_pos,self.y_pos))
        self.x_pos += dx
        self.y_pos += dy
        if (len(self.body) > self.max_size):
            del(self.body[0])