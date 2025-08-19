class Tile:
    def __init__(self, q: int, r: int, height: int = 0, env_modifiers=None, rodent=None):
        self.q = q
        self.r = r
        self.height = height
        # env_modifiers could have more than 1 component.
        self.env_modifiers = env_modifiers if env_modifiers is not None else []
        self.rodent = rodent  # Placeholder for rodent component, if any