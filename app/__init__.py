import pygame
import sys

class GameObject:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.velocity = pygame.math.Vector2(0, 0)

    def update(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def render(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)

class GameEngine:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.objects = [GameObject(100, 100, 50, 50)]

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        for obj in self.objects:
            obj.update()

    def render(self):
        self.screen.fill((0, 0, 0))
        for obj in self.objects:
            obj.render(self.screen)
        pygame.display.flip()

if __name__ == "__main__":
    game = GameEngine(800, 600)
    game.run()
    pygame.quit()
    sys.exit()
