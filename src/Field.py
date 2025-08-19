import json
from typing import List
from src.Tile import Tile
from src.hex_utils import *

# TODO: Implement the skeleton for feature-tile ownership registry.

class Field:
  def __init__(self, path: str):
    # Initialize field properties
    self.tiles = {}  # Dictionary to hold Tile objects with (x, y) as keys
    self.height = 0
    self.width = 0
    self.tile_selection_manager = TileSelectionManager()

    # Load the field from the specified path
    # Tiles, height, width are loaded from the file.
    self.load_and_compose_field(path)

  def load_and_compose_field(self, path: str):
    # Load level definition json file.
    with open(path, 'r') as file:
      data = json.load(file)

    # Extract height and width of the map.
    self.height = data["height"]
    self.width = data["width"]

    # Extract each layer definitions.
    extracted_layers = []
    for layer in data["layers"]:
      extracted_layers.append(layer["data"])

    # Convert 1D layer data to 2D arrays.
    def to_2d(data_1d: List[int], width: int, height: int) -> List[List[int]]:
      return [data_1d[i * width:(i + 1) * width] for i in range(height)]

    layers = [to_2d(layer_data, self.width, self.height) for layer_data in extracted_layers]

    # Compose the field using the extracted layers.
    self.tiles = {}
    for y in range(self.height):
      for x in range(self.width):
        # First layer defines playable space & their heights.
        # If tile_height = 0, define that tile as empty and skip to the next tile.
        tile_height = layers[0][y][x]
        if tile_height == 0:
          continue

        # Second layer defines env. modifiers
        # TODO: add code & components to define actual env. modifiers.
        modifier_id = layers[1][y][x]
        modifiers = []
        if modifier_id != 0:
          modifiers.append(modifier_id)

        # Store tile in dict with (x, y) as axial coordinates
        self.tiles[(x, y)] = Tile(q=x, r=y, height=tile_height, env_modifiers=modifiers)
  
  def place_unit(self, unit):
    tile_coords = unit.tile  
    tile = self.get_tile_at(*tile_coords)
    if tile is not None:
        if tile.unit is None:  # check occupancy
            tile.unit = unit   # assign unit to tile
        else:
            raise ValueError(f"Tile at {tile_coords} is already occupied")
    else:
        raise ValueError(f"No tile exists at coordinates {tile_coords}")
    
  # region GETTER AND SETTERS
  """
    GETTERS
  """

  def get_tile_at(self, x, y) -> Tile:
    return self.tiles.get((x, y), None)
    
  def get_selected_tile(self) -> Tile:
    return self.tile_selection_manager.selected_tile
  
  def get_hovered_tile(self) -> Tile:
    return self.tile_selection_manager.hovered_tile
  
  # Could be an attribute? IDK, we'll see.
  def get_field_center(self, hex_size: int) -> tuple[float, float]:
    import math
    SQRT3 = math.sqrt(3)

    # Total field width and height in pixels
    field_width = (self.width - 1 + 0.5) * SQRT3 * hex_size
    field_height = (self.height - 1) * 1.5 * hex_size

    # Center coordinates
    center_x = field_width / 2
    center_y = field_height / 2

    return center_x, center_y

  # endregion
  
class TileSelectionManager:
    def __init__(self):
        self.selected_tile = None
        self.hovered_tile = None

    def select(self, tile: Tile):
        self.selected_tile = tile

    def hover(self, tile: Tile):
        self.hovered_tile = tile

    def clear_selected(self):
        self.selected_tile = None

    def clear_hovered(self):
        self.hovered_tile = None


