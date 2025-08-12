import pygame
import sys
from src.Field import Field

def main():
    pygame.init()

    # Set up the window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Basic Pygame Skeleton")

    clock = pygame.time.Clock()

    field = Field("test_field.tmj")

    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # You can add more event handling here (e.g. keyboard, mouse)

        # Game logic updates go here

        # Drawing code
        screen.fill((30, 30, 30))  # Fill screen with dark gray color
        field.draw(screen, 100, 100, 30)

        # Draw stuff here

        pygame.display.flip()  # Update the full display surface to the screen

        clock.tick(60)  # Limit to 60 frames per second

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
