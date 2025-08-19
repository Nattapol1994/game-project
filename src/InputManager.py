import pygame
from src.hex_utils import *
from src.Unit import Unit

class InputManager:
    def __init__(self, camera, pan_speed=10, zoom_speed=0.1, min_zoom=0.5, max_zoom=3.0, field=None):
        self.camera = camera
        self.pan_speed = pan_speed
        self.zoom_speed = zoom_speed
        self.min_zoom = min_zoom
        self.max_zoom = max_zoom
        self.field = field  # Reference to the field for tile selection
        self.font = pygame.font.SysFont(None, 24) # Default font for rendering text

    """
    Processes all input events and updates camera and tile selection accordingly.
    """
    def process_all_events(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        world_coords = self.camera.screen_to_world(mouse_x, mouse_y)

        for event in pygame.event.get():
            if not self._handle_window_event(event):
                return False
            self._handle_mouse_event(event, world_coords)
        
        self._handle_keyboard_input()
        return True

    """
    Handles window events like quitting the game.
    Returns False if the game should exit.  
    """
    def _handle_window_event(self, event):
        if event.type == pygame.QUIT:
            return False
        return True

    """
    Handles mouse events for zooming and tile selection.
    """ 
    def _handle_mouse_event(self, event, world_coords):
        if event.type == pygame.MOUSEWHEEL:
            self._zoom(event.y)
        elif event.type == pygame.MOUSEMOTION:
            self._hover_tile(world_coords)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Left-click: select tile/unit
            if event.button == 1:
                self._select_tile(world_coords)

            # Right-click: place a new unit at the clicked tile
            elif event.button == 3:  # Right mouse button
                q, r = world_to_axial(*world_coords, self.field.hex_size)  # Adjust hex_size accordingly
                # Check if tile is empty
                if self.field.get_tile_at_world_coord(*world_coords).unit is None:
                    # Create a new Unit instance (example: default stats)
                    new_unit = Unit(
                        name="NewRodent",
                        hp=10,
                        speed=3,
                        stamina=2,
                        move_cost=1,
                        tile=(q, r),
                        crumb_cost=1,
                        defense=1,
                        attack=2,
                        height=1
                    )
                    self.field.place_unit(new_unit)
                    print(f"Placed unit at ({q}, {r})")
                else:
                    print(f"Tile at ({q}, {r}) is occupied, cannot place unit.")
        
    """
    Handles keyboard input for camera movement.
    """
    def _handle_keyboard_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.camera.x -= self.pan_speed / self.camera.zoom
        if keys[pygame.K_RIGHT]:
            self.camera.x += self.pan_speed / self.camera.zoom
        if keys[pygame.K_UP]:
            self.camera.y -= self.pan_speed / self.camera.zoom
        if keys[pygame.K_DOWN]:
            self.camera.y += self.pan_speed / self.camera.zoom

    """
    Zooms the camera in or out based on mouse wheel input.
    Clamps the zoom level between min_zoom and max_zoom.
    """
    def _zoom(self, wheel_delta):
        if wheel_delta > 0:
            self.camera.zoom = min(self.camera.zoom + self.zoom_speed, self.max_zoom)
        else:
            self.camera.zoom = max(self.camera.zoom - self.zoom_speed, self.min_zoom)

    """
    Selects a tile based on world coordinates.
    Converts world coordinates to axial coordinates and selects the tile.  
    """
    def _select_tile(self, world_coords):
        selected_tile = self.field.get_tile_at_world_coord(*world_coords)
        self.field.tile_selection_manager.select(selected_tile)

    def _hover_tile(self, world_coords):
        hovered_tile = self.field.get_tile_at_world_coord(*world_coords)
        self.field.tile_selection_manager.hover(hovered_tile)

