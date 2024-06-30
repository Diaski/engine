import pygame
class ExampleScene:
    def __init__(self, event_handler):
        self.event_handler = event_handler
        self.position = [100, 100]
        self.velocity = [0, 0]
        self.speed = 5

    def update(self):
        self.velocity = [0, 0]

        if self.event_handler.keys["up"]:
            self.velocity[1] -= self.speed
        if self.event_handler.keys["down"]:
            self.velocity[1] += self.speed
        if self.event_handler.keys["left"]:
            self.velocity[0] -= self.speed
        if self.event_handler.keys["right"]:
            self.velocity[0] += self.speed

        self.position[0] += self.velocity[0]
        self.position[1] += self.velocity[1]

    def render(self, screen):
        screen.fill((25, 25, 25))  
        pygame.draw.rect(screen, (255, 33, 30), (*self.position, 50, 50))  
