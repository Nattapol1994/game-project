import pygame
import sys
from src.Field import Field
from src.Camera import Camera
from src.InputHandler import InputHandler

def main():
    pygame.init()

    # Set up the window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Basic Pygame Skeleton")

    camera = Camera()
    clock = pygame.time.Clock()
    field = Field("test_field.tmj")
    input_handler = InputHandler(camera)

    running = True

    while running:
        running = input_handler.process_all_events()

        # Drawing
        screen.fill((30, 30, 30)) # Dark gray background
        field.draw(screen=screen, camera=camera, hex_size=30)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
