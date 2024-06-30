import pygame
from .renderer import Renderer
from .event_handler import EventHandler
from .physics_engine import PhysicsEngine
from .audio_engine import AudioEngine
from .resource_manager import ResourceManager
from .scene_manager import SceneManager
from .ecs import ECS

class GameEngine:
    def __init__(self):
        self.is_running = True
        self.clock = pygame.time.Clock()
        self.renderer = Renderer()
        self.event_handler = EventHandler()
        self.physics_engine = PhysicsEngine()
        self.audio_engine = AudioEngine()
        self.resource_manager = ResourceManager()
        self.scene_manager = SceneManager()
        self.ecs = ECS()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            self.event_handler.process_events(event)

    def update(self):
        self.physics_engine.update()

    def render(self):
        self.renderer.render(self.scene_manager.get_current_scene())

    def quit(self):
        self.is_running = False
