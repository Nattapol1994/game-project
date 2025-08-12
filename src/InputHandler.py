import pygame

class InputHandler:
    def __init__(self, camera, pan_speed=10, zoom_speed=0.1, min_zoom=0.5, max_zoom=3.0):
        self.camera = camera
        self.pan_speed = pan_speed
        self.zoom_speed = zoom_speed
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom

    def process_all_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEWHEEL:
                if event.y > 0:
                    self.camera.zoom = min(self.camera.zoom + self.zoom_speed, self.max_zoom)
                elif event.y < 0:
                    self.camera.zoom = max(self.camera.zoom - self.zoom_speed, self.min_zoom)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.camera.x -= self.pan_speed / self.camera.zoom
        if keys[pygame.K_RIGHT]:
            self.camera.x += self.pan_speed / self.camera.zoom
        if keys[pygame.K_UP]:
            self.camera.y -= self.pan_speed / self.camera.zoom
        if keys[pygame.K_DOWN]:
            self.camera.y += self.pan_speed / self.camera.zoom

        return True
