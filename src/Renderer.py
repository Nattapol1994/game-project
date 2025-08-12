import pygame

class Renderer:
    _instance = None

    @staticmethod
    def get_instance():
        if Renderer._instance is None:
            Renderer._instance = Renderer()
        return Renderer._instance

    def __init__(self):
        if Renderer._instance is not None:
            raise Exception("Renderer is a singleton!")
        # Initialize any rendering state here (e.g., screen, camera)
        self.screen = None
        self.camera_offset = (0, 0)

    def set_screen(self, screen):
        self.screen = screen

    def draw(self, game_objects):
        if self.screen is None:
            raise Exception("Screen not set for Renderer!")

        self.screen.fill((0, 0, 0))  # Clear screen

        for obj in game_objects:
            # Assume each object has a draw(self, screen, camera_offset) method
            obj.draw(self.screen, self.camera_offset)

        pygame.display.flip()
