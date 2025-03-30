from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

    def get_settings(self) -> tuple[int, int, int]:
        """
        Get the settings for the current difficulty.

        :return: tuple[int, int, int] - A tuple containing rows, cols, and mines.
        """
        settings = {
            Difficulty.EASY: (9, 9, 10),
            Difficulty.MEDIUM: (16, 16, 40),
            Difficulty.HARD: (16, 30, 99)
        }
        return settings[self]
