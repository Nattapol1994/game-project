import pygame
import sys
from src.Field import Field
from src.Camera import Camera
from src.InputManager import InputManager
from src.hex_utils import *
from src.Renderer import Renderer

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
    # Create the camera, then center it on the field's center
    field = Field("test_field.tmj")
    field_center_x, field_center_y = field.get_field_center(hex_size=HEX_SIZE)
    camera = Camera(x = field_center_x, y = field_center_y, screen_width=screen_width, screen_height=screen_height)
    input_manager = InputManager(camera=camera, field=field)
    renderer = Renderer(screen=screen, camera=camera, hex_size=HEX_SIZE)

    running = True

    while running:
        running = input_manager.process_all_events()

        # Drawing
        renderer.render(screen, field, [], [])

        # TODO: Create debug message pipeline to separate input and rendering logic.
        # # Get mouse position in screen coordinates
        # mouse_x, mouse_y = pygame.mouse.get_pos()
        # # Convert to world coordinates using the camera
        # world_coords = camera.screen_to_world(mouse_x, mouse_y)
        # # Render the world coordinates as text
        # font = pygame.font.SysFont(None, 24)
        # coord_text = font.render(f"World coordinate: {world_coords}", True, (255, 255, 255))
        # screen.blit(coord_text, (10, 10))

        # # Convert world coordinates to hex tile coordinates
        # hex_coords = world_to_axial(world_coords[0], world_coords[1], HEX_SIZE)
        # hex_text = font.render(f"Hovering tile: {hex_coords}", True, (255, 255, 0))
        # screen.blit(hex_text, (10, 40))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
