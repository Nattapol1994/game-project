import math

"""Utility functions for hexagonal grid calculations.
These functions handle conversions between axial coordinates and world coordinates,"""

SQRT3 = math.sqrt(3)

"""Convert axial coordinates (q, r) to world coordinates (x, y).
Args:
    q (int): Axial coordinate q.
    r (int): Axial coordinate r.
    center_x (float): X coordinate of the center of the hex grid.
    center_y (float): Y coordinate of the center of the hex grid.
    size (float): Size of the hexagon."""
def axial_to_world(q, r, center_x, center_y, size):
    x = size * SQRT3 * (q + 0.5 * (r % 2)) + center_x  # stagger odd rows by 0.5
    y = size * 1.5 * r + center_y
    return x, y
  
"""Convert world coordinates (world_x, world_y) to axial coordinates (q, r).
Args:   
    world_x (float): X coordinate in world space.
    world_y (float): Y coordinate in world space.
    hex_size (float): Size of the hexagon."""
def world_to_axial(world_x, world_y, hex_size):
    # Shift world coordinates so 0,0 is the **center** of the first hex
    shifted_x = world_x + 0.5 * SQRT3 * hex_size
    shifted_y = world_y + 0.5 * 1.5 * hex_size

    # Approximate row first
    r = int(shifted_y // (1.5 * hex_size))

    # Approximate column, adjust for row staggering
    q = int((shifted_x - 0.5 * (r % 2) * SQRT3 * hex_size) // (SQRT3 * hex_size))

    return q, r

"""
    Return a list of 6 (x, y) points for the corners of a hex
    at axial coords (q, r), sized by hex_size.
"""
def hex_corners(q: int, r: int, hex_size: int) -> list[tuple[float, float]]:
    cx, cy = axial_to_world(q, r, 0, 0, hex_size)  # center of hex
    corners = []
    for i in range(6):
        angle_deg = 60 * i - 30  # flat-top orientation
        angle_rad = math.radians(angle_deg)
        x = cx + hex_size * math.cos(angle_rad)
        y = cy + hex_size * math.sin(angle_rad)
        corners.append((x, y))
    return corners