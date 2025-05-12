# Existing config content
WAYPOINTS = [
    {"x": 100, "y": 200},
    {"x": 105, "y": 205},
]

KEY_BINDINGS = {
    "move_up": "w",
    "move_down": "s",
    "move_left": "a",
    "move_right": "d",
    "attack_spell": "q",
    "heal_spell": "e",
    "rune_creation": "r",
    "use_rune": "f",  # Default rune hotkey, user can change this
}

# Rune configuration
RUNE_CONFIG = {
    "enabled": True,
    "target_delay_min": 0.2,  # Minimum delay before clicking target after hotkey
    "target_delay_max": 0.4,  # Maximum delay before clicking target
}

HP_LOW_THRESHOLD = 50
MANA_LOW_THRESHOLD = 30

# Delays (in seconds) to mimic human-like random intervals:
DELAY_MIN = 0.5
DELAY_MAX = 1.5
