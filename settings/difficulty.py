from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3

    @classmethod
    def get_settings(cls, difficulty: "Difficulty") -> tuple[int, int, int]:
        """
        Get the settings for the specified difficulty.

        :param difficulty: Difficulty - The difficulty level.
        :return: tuple[int, int, int] - A tuple containing rows, cols, and mines.
        """
        settings = {
            cls.EASY: (9, 9, 10),
            cls.MEDIUM: (16, 16, 40),
            cls.HARD: (16, 30, 99)
        }
        return settings[difficulty]
