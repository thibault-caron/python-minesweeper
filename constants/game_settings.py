from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

# Centralized difficulty settings
difficulty_settings = {
    Difficulty.EASY: (9, 9, 10),
    Difficulty.MEDIUM: (16, 16, 40),
    Difficulty.HARD: (16, 30, 99)
}
