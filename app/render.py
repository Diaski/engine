import pygame
class Renderer:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600))

    def render(self, scene):
        self.screen.fill((0, 0, 0))  # Clear screen with black
        # Render all objects in the scene
        pygame.display.flip()
