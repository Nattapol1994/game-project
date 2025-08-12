class Camera:
    def __init__(self, x=0, y=0, zoom=1.0, screen_width=800, screen_height=600):
        self.x = x  # World position center X
        self.y = y  # World position center Y
        self.zoom = zoom  # Zoom scale factor
        self.screen_width = screen_width
        self.screen_height = screen_height

    @property
    def screen_center_x(self):
        return self.screen_width / 2

    @property
    def screen_center_y(self):
        return self.screen_height / 2

    def world_to_screen(self, wx, wy):
        """
        Convert world coordinates (wx, wy) to screen coordinates (sx, sy).
        Applies zoom and camera position, and centers the view on screen.
        """
        sx = (wx - self.x) * self.zoom + self.screen_center_x
        sy = (wy - self.y) * self.zoom + self.screen_center_y
        return sx, sy

    def screen_to_world(self, sx, sy):
        """
        Convert screen coordinates (sx, sy) back to world coordinates (wx, wy).
        Reverses zoom and camera position transformations.
        """
        wx = (sx - self.screen_center_x) / self.zoom + self.x
        wy = (sy - self.screen_center_y) / self.zoom + self.y
        return wx, wy

    def move(self, dx, dy):
        """
        Move the camera's world position by (dx, dy).
        """
        self.x += dx
        self.y += dy

    def set_zoom(self, zoom):
        """
        Set zoom level, clamping to reasonable limits.
        """
        self.zoom = max(0.1, min(zoom, 5.0))  # Clamp zoom between 0.1 and 5.0

    def zoom_by(self, factor):
        """
        Zoom in/out by multiplying current zoom by factor.
        """
        self.set_zoom(self.zoom * factor)
