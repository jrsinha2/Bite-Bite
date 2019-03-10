import pygame
from src.Config import Config
from src.Snake import Snake
from src.Apple import Apple
class Game:
    def __init__(self,display):  #constructor
        self.display = display
        self.score = 0
    
    def start_screen(self):
        clock = pygame.time.Clock() #get time (initializing time)
        self.display.fill(Config['colors']['green']) #wipe old position  
        pygame.draw.rect(self.display,Config['colors']['black'],[ 
                Config['game']['bumper_size'],
                Config['game']['bumper_size'],
                Config['game']['height'] - Config['game']['bumper_size']*2,
                Config['game']['width'] - Config['game']['bumper_size']*2 ] )
        text = "Welcome to Bite-Bite"
        pygame.font.init()
        font = pygame.font.Font('./assets/Now-Regular.otf',28)  #load font from assets #font in object
        start_text = font.render(text,True,Config['colors']['white'])
        start_text_rect = start_text.get_rect(
                center = (
                    Config['game']['width']/2,   #width of box
                    Config['game']['height']/2  #height of box
                )
            )
        self.display.blit(start_text,start_text_rect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.loop()
                
                    
            pygame.display.update()
            clock.tick(Config['game']['fps']) #to slow time rate (30 frames per second)
    
    
    def loop(self):
        clock = pygame.time.Clock() #get time (initializing time)
        apple = Apple(self.display)
        snake = Snake(self.display)
        x_change = 0
        y_change = 0
        self.score = 0   
        while True:
            #pygame.event.get() returns all the events in queue
            #so we are iterating such events in queue
            for event in pygame.event.get():    #user input events
                if event.type == pygame.QUIT:   #type such as mouse,keyboard,exit the application
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change  = -Config['snake']['speed']
                        y_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x_change = Config['snake']['speed']
                        y_change = 0
                    elif event.key == pygame.K_UP:
                        y_change = -Config['snake']['speed']
                        x_change = 0
                    elif event.key == pygame.K_DOWN:
                        y_change = Config['snake']['speed']
                        x_change = 0
            
            self.display.fill(Config['colors']['green']) #wipe old position  
            pygame.draw.rect(self.display,Config['colors']['black'],[ 
                Config['game']['bumper_size'],
                Config['game']['bumper_size'],
                Config['game']['height'] - Config['game']['bumper_size']*2,
                Config['game']['width'] - Config['game']['bumper_size']*2 ] )
            apple_rect = apple.draw()
            snake.move(x_change,y_change)   
            snake_rect = snake.draw()  #
            bumper_x = Config['game']['width'] - Config['game']['bumper_size']
            bumper_y = Config['game']['height'] - Config['game']['bumper_size']
            if (    snake.x_pos < 30 or 
                    snake.y_pos < 30 or
                    snake.x_pos + Config['snake']['width'] > bumper_x or
                    snake.y_pos + Config['snake']['height'] > bumper_y
            ):
                self.end_screen(self.score)
            if apple_rect.colliderect(snake_rect): #pygame colliderect checks if two rectangles overlap
                apple.randomize()
                snake.eat()
                self.score += 1
            if len(snake.body)>=1:
                for cell in snake.body:
                    if snake.x_pos == cell[0] and snake.y_pos == cell[1]:
                        self.end_screen(self.score)

            pygame.font.init()
            font = pygame.font.Font('./assets/Now-Regular.otf',28)  #load font from assets #font in object

            score_text = 'Score: {} '.format(self.score)
            score = font.render(score_text,True,Config['colors']['white'])  
            title = font.render('Bite-Bite',True,Config['colors']['white'])
            #render is method of font (accepts the input string,boolean value (for anti aliasing),RGB value)


            title_rect = title.get_rect(
                center = (
                    Config['game']['width']/2,   #width of box
                    Config['game']['bumper_size']/2  #height of box
                )
            )

            score_rect = score.get_rect(
                center = (
                    Config['game']['width']/2,
                    Config['game']['height']-Config['game']['bumper_size']/2
                )
            )
            #get_rect gives the bounding box size around the text 
            self.display.blit(score,score_rect)
            self.display.blit(title,title_rect)
            
            pygame.display.update()
            clock.tick(Config['game']['fps']) #to slow time rate (30 frames per second) 

    def end_screen(self,score):
        clock = pygame.time.Clock() #get time (initializing time)
        self.display.fill(Config['colors']['green']) #wipe old position  
        pygame.draw.rect(self.display,Config['colors']['black'],[ 
                Config['game']['bumper_size'],
                Config['game']['bumper_size'],
                Config['game']['height'] - Config['game']['bumper_size']*2,
                Config['game']['width'] - Config['game']['bumper_size']*2 ] )
        
        text = "Game Over Your Score : {}".format(score)
        pygame.font.init()
        font = pygame.font.Font('./assets/Now-Regular.otf',28)  #load font from assets #font in object
        end_text = font.render(text,True,Config['colors']['white'])
        end_text_rect = end_text.get_rect(
                center = (
                    Config['game']['width']/2,   #width of box
                    Config['game']['height']/2  #height of box
                )
            )
        self.display.blit(end_text,end_text_rect)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.loop()
                    
            pygame.display.update()
            clock.tick(Config['game']['fps']) #to slow time rate (30 frames per second)
    