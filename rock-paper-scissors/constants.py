# constants.py

# By convention, constants are UPPERCASE.
ROCK = "r"
PAPER = "p"
SCISSORS = "s"

# Emoji mapping (single source of truth)
EMOJIS = {
    ROCK: "🪨",
    PAPER: "📄",
    SCISSORS: "✂️",
}

# Valid choices derived from EMOJIS (DRY)
CHOICES = tuple(EMOJIS.keys())
