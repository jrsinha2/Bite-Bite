import pygame
from src.Config import Config
from src.Snake import Snake
from src.Apple import Apple
class Game:
    def __init__(self,display):  #constructor
        self.display = display
        self.score = 0
        self.pause = False
    
    def start_screen(self):
        clock = pygame.time.Clock() #get time (initializing time)
        self.display.fill(Config['colors']['brown']) #wipe old position  
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
                    Config['game']['height']/4  #height of box
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
            mouse = pygame.mouse.get_pos()
            start_menu_pos_x = Config['game']['width']/2
            start_menu_pos_y = 4*Config['game']['height']/8
            start_menu_height = Config['game']['height']*0.1
            start_menu_width =  Config['game']['width']*0.25
            start_menu_text = "Play"
            
            quit_menu_pos_x = Config['game']['width']/2
            quit_menu_pos_y = 6*Config['game']['height']/8
            quit_menu_height = Config['game']['height']*0.1
            quit_menu_width =  Config['game']['width']*0.25
            quit_menu_text = "Quit"
            
            #interactive buttons
            self.button(start_menu_text,start_menu_pos_x,start_menu_pos_y,start_menu_width,start_menu_height,Config['colors']['green'],Config['colors']['bright_green'],Config['colors']['white'],self.loop)
            self.button(quit_menu_text,quit_menu_pos_x,quit_menu_pos_y,quit_menu_width,quit_menu_height,Config['colors']['red'],Config['colors']['bright_red'],Config['colors']['white'],exit)
            
            '''if start_menu_pos_x + start_menu_width/2 > mouse[0] > start_menu_pos_x-start_menu_width/2 and  start_menu_pos_y + start_menu_height/2 > mouse[1] > start_menu_pos_y- start_menu_height/2 :
                pygame.draw.rect(self.display,Config['colors']['bright_green'],
                (start_menu_pos_x-start_menu_width/2,start_menu_pos_y- start_menu_height/2,start_menu_width,start_menu_height))
            else:
                pygame.draw.rect(self.display,Config['colors']['green'],
                (start_menu_pos_x-start_menu_width/2,start_menu_pos_y- start_menu_height/2,start_menu_width,start_menu_height))
            
            if quit_menu_pos_x + quit_menu_width/2 > mouse[0] > quit_menu_pos_x-quit_menu_width/2 and  quit_menu_pos_y + quit_menu_height/2 > mouse[1] > quit_menu_pos_y- quit_menu_height/2 :
                pygame.draw.rect(self.display,Config['colors']['bright_red'],
                (quit_menu_pos_x-quit_menu_width/2,quit_menu_pos_y- quit_menu_height/2,quit_menu_width,quit_menu_height))
            else:
                pygame.draw.rect(self.display,Config['colors']['red'],
                (quit_menu_pos_x-quit_menu_width/2,quit_menu_pos_y- quit_menu_height/2,quit_menu_width,quit_menu_height))
            
            #displaying text on buttons
            start_menu_text_object = font.render(start_menu_text,True,Config['colors']['white'])
            start_menu_text_rect = start_menu_text_object.get_rect(
                center = (start_menu_pos_x,start_menu_pos_y)
            )
            self.display.blit(start_menu_text_object, start_menu_text_rect)

            quit_menu_text_object = font.render(quit_menu_text,True,Config['colors']['white'])
            quit_menu_text_rect = quit_menu_text_object.get_rect(
                center = (quit_menu_pos_x,quit_menu_pos_y)
            )
            self.display.blit(quit_menu_text_object, quit_menu_text_rect)
            '''

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
                    if event.key == pygame.K_ESCAPE:
                        self.pause = True
                        self.paused(Config['game']['width']/2,Config['game']['height']/4,Config['game']['width']*0.25,Config['game']['height']*0.1,Config['colors']['white'])
                        #print("Came out of pause")
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
            
            self.display.fill(Config['colors']['brown']) #wipe old position  
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
        self.display.fill(Config['colors']['brown']) #wipe old position  
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
                        self.start_screen()
                    
            pygame.display.update()
            clock.tick(Config['game']['fps']) #to slow time rate (30 frames per second)
    
    def button(self,text,pos_x,pos_y,width,height,inactive_color,active_color,text_color,action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if pos_x + width/2 > mouse[0] > pos_x-width/2 and  pos_y + height/2 > mouse[1] > pos_y- height/2 :
            pygame.draw.rect(self.display,active_color,
            (pos_x-width/2,pos_y- height/2,width,height))
            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(self.display,inactive_color,
            (pos_x-width/2,pos_y- height/2,width,height))
        
        pygame.font.init()
        font = pygame.font.Font('./assets/Now-Regular.otf',28)
        start_menu_text_object = font.render(text,True,text_color)
        start_menu_text_rect = start_menu_text_object.get_rect(
                    center = (pos_x,pos_y)
                )
        self.display.blit(start_menu_text_object, start_menu_text_rect)

    def paused(self,pos_x,pos_y,width,height,text_color):
        
        pygame.font.init()
        font = pygame.font.Font('./assets/Now-Regular.otf',28)
        start_menu_text_object = font.render("Paused",True,text_color)
        start_menu_text_rect = start_menu_text_object.get_rect(
                    center = (pos_x,pos_y)
                )
        self.display.blit(start_menu_text_object, start_menu_text_rect)
        clock = pygame.time.Clock()
        while self.pause ==True :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        self.unpause()
            self.button("Quit",pos_x,pos_y+150,width,height,Config['colors']['red'],Config['colors']['bright_red'],text_color,exit)
            self.button("Continue",pos_x,pos_y+50,width,height,Config['colors']['green'],Config['colors']['bright_green'],text_color,self.unpause)
            pygame.display.update()
            clock.tick(15)
    
        

    def unpause(self):
        self.pause = False
     