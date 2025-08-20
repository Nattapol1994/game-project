import pygame
import sys
from src.Field import Field
from src.Camera import Camera
from src.InputManager import InputManager
from src.hex_utils import *
from src.Renderer import Renderer

# TODO: Create debug message pipeline?
# FIXME: Sometimes clicking pixel-perfectly between two tiles select a tile different from the one that was highlighted.

def main():
    pygame.init()

    # Temporary tile size
    HEX_SIZE = 30  # Size of hex tiles in pixels

    # Set up the window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Basic Pygame Skeleton")
    clock = pygame.time.Clock()

    # Load the field
    field = Field("test_field.tmj", hex_size=HEX_SIZE)

    # Set-up camera, input manager, and renderer
    field_center_x, field_center_y = field.get_field_center()
    camera = Camera(x = field_center_x, y = field_center_y, screen_width=screen_width, screen_height=screen_height)
    input_manager = InputManager(camera=camera, field=field)
    renderer = Renderer(screen=screen, camera=camera, field_hex_size=field.hex_size)

    running = True

    while running:
        running = input_manager.process_all_events()

        # Drawing
        renderer.render(screen, field, [], [])

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
