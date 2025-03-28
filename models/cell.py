class Cell:
    """
    Represents a single cell in the Minesweeper grid.

    :param row: int - Row index of the cell.
    :param col: int - Column index of the cell.
    """
    def __init__(self, row: int, col: int):
        self.__row: int = row
        self.__col: int = col
        self.__is_mine: bool = False
        self.__is_revealed: bool = False
        self.__is_flagged: bool = False
        self.__is_unsure: bool = False
        self.__adjacent_mines: int = 0

    # Properties
    @property
    def row(self) -> int:
        return self.__row

    @property
    def col(self) -> int:
        return self.__col

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    @property
    def is_revealed(self) -> bool:
        return self.__is_revealed

    @property
    def is_flagged(self) -> bool:
        return self.__is_flagged

    @property
    def is_unsure(self) -> bool:
        return self.__is_unsure

    @property
    def adjacent_mines(self) -> int:
        return self.__adjacent_mines

    # Setters
    @is_mine.setter
    def is_mine(self, value: bool) -> None:
        self.__is_mine = value

    @is_revealed.setter
    def is_revealed(self, value: bool) -> None:
        self.__is_revealed = value

    @is_flagged.setter
    def is_flagged(self, value: bool) -> None:
        self.__is_flagged = value

    @is_unsure.setter
    def is_unsure(self, value: bool) -> None:
        self.__is_unsure = value

    @adjacent_mines.setter
    def adjacent_mines(self, value: int) -> None:
        self.__adjacent_mines = value

    # Methods
    def __repr__(self) -> str:
        """
        Return a string representation of the cell.

        :return: str - String representation of the cell.
        """
        return f"Cell({self.__row}, {self.__col}, Mine={self.__is_mine}, Flagged={self.__is_flagged}, Unsure={self.__is_unsure})"
