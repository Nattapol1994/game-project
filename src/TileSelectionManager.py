from src.Tile import Tile

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