import pygame

from src.Config import Config
from src.Game import Game  # importing Game Class


def main():
    display = pygame.display.set_mode((Config['game']['height'],Config['game']['width']))    
    pygame.display.set_caption(Config['game']['caption'])
    #create a 800x600 pixel game window with title
    
    
    game = Game(display)    #pass reference to display into game object
    game.start_screen()

if __name__ == '__main__':
    main()
