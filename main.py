import pygame
from engine.core import GameEngine
from scenes.scene_registry import register_scenes

if __name__ == "__main__":
    pygame.init()

    game = GameEngine()

    register_scenes(game.scene_manager)
    
    game.scene_manager.load_scene("example")

    game.run()

    pygame.quit()
