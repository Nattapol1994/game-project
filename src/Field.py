import json
from typing import List
from src.Tile import Tile
import pygame
import math
from src.Camera import Camera

class Field:
  def __init__(self, path: str):
    self.height = 0
    self.width = 0
    layers = self.load_data(path)
    self.compose_field(layers=layers)

  def load_data(self, path: str) -> List[List[List[int]]]:
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

    # Return the extracted layer definitions as 2D arrays.
    def to_2d(data_1d: List[int], width: int, height: int) -> List[List[int]]:
      return [data_1d[i * width:(i + 1) * width] for i in range(height)]

    extracted_layers_2d = [to_2d(layer_data, self.width, self.height) for layer_data in extracted_layers]
    return extracted_layers_2d

  def compose_field(self, layers: List[List[List[int]]]) -> None:
    self.tiles = []
    for y in range(self.height):
      row = []
      for x in range(self.width):
        # First layer defines playable space & their heights.
        # If tile_height = 0, define that tile as empty and skip to the next tile.
        tile_height = layers[0][y][x]
        if tile_height == 0:
          row.append(None)
          continue

        # Second layer defines env. modifiers
        # TODO: add code & components to define actual env. modifiers.
        modifier_id = layers[1][y][x]
        modifiers = []
        if modifier_id != 0:
          modifiers.append(modifier_id)

        tile = Tile(height=tile_height, env_modifiers=modifiers)
        row.append(tile)

      self.tiles.append(row)

  def draw(self, screen: pygame.Surface, camera: Camera, hex_size: int):
    font = pygame.font.SysFont(None, 24)  # create font once

    for y in range(self.height):
      for x in range(self.width):
        tile = self.tiles[y][x]
        if tile is None:
          continue

        # Calculate tile world position (axial to pixel)
        q, r = x, y
        wx, wy = self.axial_to_pixel(q, r, 0, 0, hex_size)  # World coords relative to origin (0,0)

        # Convert world coords to screen coords using camera
        sx, sy = camera.world_to_screen(wx, wy)

        # Now draw tile at screen coords
        tile.draw(screen, sx, sy, hex_size, font)

  def axial_to_pixel(self, q, r, center_x, center_y, size):
    import math
    SQRT3 = math.sqrt(3)
    x = size * SQRT3 * (q + 0.5 * (r & 1)) + center_x  # stagger odd rows by 0.5
    y = size * 1.5 * r + center_y
    return x, y
