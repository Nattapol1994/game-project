from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Tile:
    q: int
    r: int
    height: int = 0
    env_modifiers: list = field(default_factory=list)
    unit: Optional[object] = None  # could be Unit or None
