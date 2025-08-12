import pygame

class Tile:
    def __init__(self, height: int = 0, env_modifiers=None, unit=None):
        self.height = height
        # env_modifiers could have more than 1 component.
        self.env_modifiers = env_modifiers if env_modifiers is not None else []
        self.unit = unit

    def is_occupied(self):
        return self.unit is not None
    
    def draw(self, screen: pygame.Surface, cx: int, cy: int, size: int, font: pygame.font.Font, zoom: float):
        # Adjust rect size according to zoom
        rect_size = int(size * zoom)
        rect = pygame.Rect(0, 0, rect_size, rect_size)
        rect.center = (int(cx), int(cy))

        # Example color based on height
        color = (0, 25 * self.height, 0)
        pygame.draw.rect(screen, color, rect)

        # Draw env modifier ID if exists
        if self.env_modifiers:
            mod_id = str(self.env_modifiers[0])  # first modifier id as string
            text_surf = font.render(mod_id, True, (255, 255, 255))  # white text

            # Scale text position accordingly
            text_rect = text_surf.get_rect(center=(int(cx), int(cy)))
            screen.blit(text_surf, text_rect)