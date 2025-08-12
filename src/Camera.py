class Camera:
    def __init__(self, x=0, y=0, zoom=1.0):
        self.x = x
        self.y = y
        self.zoom = zoom

    def world_to_screen(self, wx, wy):
        # Convert world (game) coordinates to screen pixels
        sx = (wx - self.x) * self.zoom
        sy = (wy - self.y) * self.zoom
        return sx, sy

    def screen_to_world(self, sx, sy):
        # Convert screen pixels back to world coordinates
        wx = sx / self.zoom + self.x
        wy = sy / self.zoom + self.y
        return wx, wy