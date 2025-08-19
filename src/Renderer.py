import pygame
from src.hex_utils import *

class Renderer:
    def __init__(self, screen, camera, field_hex_size):
        self.screen = screen
        self.camera = camera
        self.hex_size = field_hex_size
        self.font = pygame.font.SysFont(None, 24)  # Default font for rendering text

    def render(self, screen, field, units, effects):
        # Clear background
        screen.fill((30, 30, 30))

        # Delegate to smaller functions
        self.render_field(screen, field)
        self.render_units(screen, field)
        # self.render_effects(screen, effects)

        # Highlight hovered tile
        hov = field.get_hovered_tile()
        if hov:
            self.draw_tile_highlight(screen, hov, color=(0, 200, 255))

        # Highlight selected tile
        sel = field.get_selected_tile()
        if sel:
            self.draw_tile_highlight(screen, sel, color=(255, 255, 0))

    def render_field(self, screen, field):
        for tile in field.tiles.values():
            self.draw_tile(screen, tile)

    def draw_tile(self, screen, tile):
        # Preprocess tile position and size through camera parameters.
        world_x, world_y = axial_to_world(tile.q, tile.r, 0, 0, self.hex_size)
        screen_x, screen_y = self.camera.world_to_screen(world_x, world_y)
        rect_size = int(self.hex_size * self.camera.zoom)
        
        # Create a rect for the tile
        rect = pygame.Rect(0, 0, rect_size, rect_size)
        rect.center = (int(screen_x), int(screen_y))

        # Example color based on height
        color = (0, 25 * tile.height, 0)
        pygame.draw.rect(screen, color, rect)

        # Draw env modifier ID if exists
        if tile.env_modifiers:
            mod_id = str(tile.env_modifiers[0])  # first modifier id as string
            text_surf = self.font.render(mod_id, True, (255, 255, 255))  # white text

            # Scale text position accordingly
            text_rect = text_surf.get_rect(center=(int(screen_x), int(screen_y)))
            screen.blit(text_surf, text_rect)

    def draw_tile_highlight(self, screen, tile, color=(255, 255, 0), width=3):
        """
        Draw a hex highlight around the tile, respecting camera zoom and offset.
        """
        # Get world position of the tile center
        world_x, world_y = axial_to_world(tile.q, tile.r, 0, 0, self.hex_size)
        
        # Convert to screen coordinates using camera
        screen_x, screen_y = self.camera.world_to_screen(world_x, world_y)
        
        # Scale hex size according to camera zoom
        zoomed_size = self.hex_size * self.camera.zoom
        
        # Get corners for flat-top hex
        corners = []
        for i in range(6):
            angle_deg = 60 * i - 30  # flat-top
            angle_rad = math.radians(angle_deg)
            x = screen_x + zoomed_size * math.cos(angle_rad)
            y = screen_y + zoomed_size * math.sin(angle_rad)
            corners.append((x, y))
        
        # Draw the polygon outline
        pygame.draw.polygon(screen, color, corners, width)

    def draw_text(self, text, position, color=(255, 255, 255)):
        """
        Draw text on the screen at the specified position.
        """
        text_surf = self.font.render(text, True, color)
        self.screen.blit(text_surf, position)

    def draw_unit_placeholder(self, screen, tile, color=(200, 50, 50)):
        """
        Draw a unit placeholder (e.g., a circle) on top of the tile.
        Respects camera zoom and offset.
        """
        # Get tile center in world coordinates
        world_x, world_y = axial_to_world(tile.q, tile.r, 0, 0, self.hex_size)

        # Convert to screen coordinates via camera
        screen_x, screen_y = self.camera.world_to_screen(world_x, world_y)

        # Size scaled by camera zoom
        radius = int(self.hex_size * 0.5 * self.camera.zoom)  # half the tile size

        # Draw circle
        pygame.draw.circle(screen, color, (int(screen_x), int(screen_y)), radius)

    def render_units(self, screen, field):
        for tile in field.tiles.values():
            if hasattr(tile, "unit") and tile.unit is not None:
                self.draw_unit_placeholder(screen, tile)

    # def render_effects(self, screen, effects):
    #     for effect in effects:
    #         self.draw_effect(screen, effect)

    # def draw_unit(self, screen, unit):
    #     world_x, world_y = axial_to_world(unit.q, unit.r, self.hex_size)
    #     screen_x, screen_y = self.camera.world_to_screen(world_x, world_y)
    #     screen.blit(unit.sprite, (screen_x, screen_y))

    # def draw_effect(self, screen, effect):
    #     # Similar: transform → draw effect
    #     pass