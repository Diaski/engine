import pygame
from app import GameEngine
if __name__ == "__main__":
    pygame.init()
    game = GameEngine()
    game.run()
    
    pygame.quit()
