import pygame
class EventHandler:
    def __init__(self):
        self.keys = {
            "up": False,
            "down": False,
            "left": False,
            "right": False
        }
        self.key_map_movement = {
            pygame.K_w: "up",
            pygame.K_s: "down",
            pygame.K_a: "left",
            pygame.K_d: "right",
            pygame.K_UP: "up",
            pygame.K_DOWN: "down",
            pygame.K_LEFT: "left",
            pygame.K_RIGHT: "right",
        }

    def process_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                quit()
            elif event.key in self.key_map_movement:
                self.keys[self.key_map_movement[event.key]] = True
        elif event.type == pygame.KEYUP:
            if event.key in self.key_map_movement:
                self.keys[self.key_map_movement[event.key]] = False