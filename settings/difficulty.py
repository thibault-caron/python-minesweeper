from enum import Enum

class Difficulty(Enum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    CUSTOM = 4  # Add a custom difficulty option

    def get_settings(self) -> tuple[int, int, int]:
        """
        Get the settings for the current difficulty.

        :return: tuple[int, int, int] - A tuple containing rows, cols, and mines.
        """
        settings = {
            Difficulty.EASY: (8, 8, 10),
            Difficulty.MEDIUM: (16, 16, 40),
            Difficulty.HARD: (16, 30, 99),
            Difficulty.CUSTOM: CustomDifficulty.get_settings()  # Use custom settings
        }
        return settings[self]


class CustomDifficulty:
    """
    Manages custom difficulty settings.
    """
    _rows: int = 8
    _cols: int = 8
    _mines: int = 10

    @classmethod
    def set_settings(cls, rows: int, cols: int, mines: int) -> None:
        """
        Set the custom settings for the CUSTOM difficulty.

        :param rows: int - Number of rows.
        :param cols: int - Number of columns.
        :param mines: int - Number of mines.
        """
        cls._rows = rows
        cls._cols = cols
        cls._mines = mines

    @classmethod
    def get_settings(cls) -> tuple[int, int, int]:
        """
        Get the current custom settings.

        :return: tuple[int, int, int] - A tuple containing rows, cols, and mines.
        """
        return cls._rows, cls._cols, cls._mines
