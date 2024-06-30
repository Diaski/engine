import pygame
class ExampleScene:
    def __init__(self):
        pass

    def update(self):
        pass

    def render(self, screen):
        screen.fill((0, 0, 0))  
        pygame.draw.rect(screen, (255, 0, 0), (50, 50, 100, 100))  
