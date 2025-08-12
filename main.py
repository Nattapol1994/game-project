import pygame
import sys
from src.Field import Field
from src.Camera import Camera

def main():
    pygame.init()

    # Set up the window
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Basic Pygame Skeleton")

    camera = Camera()

    clock = pygame.time.Clock()

    field = Field("test_field.tmj")

    running = True
    pan_speed = 10  # pixels to move per key press
    zoom_speed = 0.1  # zoom increment per scroll
    min_zoom = 0.5
    max_zoom = 3.0

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            elif event.type == pygame.MOUSEWHEEL:
                # Zoom in/out with mouse wheel
                camera.zoom += event.y * zoom_speed
                camera.zoom = max(min_zoom, min(max_zoom, camera.zoom))
        
        # Key states for smooth panning
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            camera.x -= pan_speed / camera.zoom  # divide by zoom for consistent speed
        if keys[pygame.K_RIGHT]:
            camera.x += pan_speed / camera.zoom
        if keys[pygame.K_UP]:
            camera.y -= pan_speed / camera.zoom
        if keys[pygame.K_DOWN]:
            camera.y += pan_speed / camera.zoom

        # Drawing
        screen.fill((30, 30, 30))
        field.draw(screen=screen, camera=camera, hex_size=30)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
