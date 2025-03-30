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

    MIN_ROWS = 5
    MAX_ROWS = 22
    MIN_COLS = 5
    MAX_COLS = 45
    MIN_MINES = 5

    @classmethod
    def set_settings(cls, rows: int, cols: int, mines: int) -> None:
        """
        Set the custom settings for the CUSTOM difficulty.

        :param rows: int - Number of rows.
        :param cols: int - Number of columns.
        :param mines: int - Number of mines.
        :raises ValueError: If the provided values are out of range or invalid.
        """
        if not (cls.MIN_ROWS <= rows <= cls.MAX_ROWS):
            raise ValueError(f"Rows must be between {cls.MIN_ROWS} and {cls.MAX_ROWS}.")
        if not (cls.MIN_COLS <= cols <= cls.MAX_COLS):
            raise ValueError(f"Columns must be between {cls.MIN_COLS} and {cls.MAX_COLS}.")
        max_mines = rows * cols - 1
        if not (cls.MIN_MINES <= mines <= max_mines):
            raise ValueError(f"Mines must be between {cls.MIN_MINES} and {max_mines} for the given grid size.")

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

    @classmethod
    def validate_settings(cls, rows: int, cols: int, mines: int) -> bool:
        """
        Validate the custom settings without applying them.

        :param rows: int - Number of rows.
        :param cols: int - Number of columns.
        :param mines: int - Number of mines.
        :return: bool - True if the settings are valid, False otherwise.
        """
        try:
            cls.set_settings(rows, cols, mines)
            return True
        except ValueError:
            return False
