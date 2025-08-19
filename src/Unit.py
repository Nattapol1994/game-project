from dataclasses import dataclass, field

@dataclass
class Unit:
    name: str
    crumb_cost: int # How many crumbs are needed to play this unit
    hp: int
    speed: int      # How far can this unit move when a movement action is taken
    stamina: int    # How many movement action can this unit take in a turn
    move_cost: int  # How many crumbs are consumed per movement action
    defense: int    # Reduces incoming damage by this amount
    attack: int     # How much damage this unit deals when attacking. Base reference amount for other skills.
    height: int     # How tall this unit is, used for height-based interactions

    # Runtime state
    current_hp: int = None
    current_stamina: int = None
    tile: tuple = None  # Axial coordinates (q, r)

    # Optional components for future extensibility
    skills: list = field(default_factory=list)
    ai_component: object = None
    sprite_sheet: object = None

    def __post_init__(self):
        self.current_hp = self.hp
        self.current_stamina = self.stamina

    def move_to(self, target_tile, crumbs_available):
        if self.current_stamina <= 0 or crumbs_available < self.move_cost:
            return False
        self.tile = target_tile
        self.current_stamina -= 1
        return True

    def take_damage(self, damage):
        damage_taken = max(0, damage - self.defense)
        self.current_hp -= damage_taken
        return damage_taken

    def reset_for_new_turn(self):
        self.current_stamina = self.stamina
