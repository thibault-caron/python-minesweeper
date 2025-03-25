class Cell:
    """
    Represents a single cell in the Minesweeper grid.

    :param row: int - Row index of the cell.
    :param col: int - Column index of the cell.
    """
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col
        self.is_mine: bool = False
        self.is_revealed: bool = False
        self.is_flagged: bool = False
        self.is_unsure: bool = False
        self.adjacent_mines: int = 0

    def __repr__(self) -> str:
        """
        Return a string representation of the cell.

        :return: str - String representation of the cell.
        """
        return f"Cell({self.row}, {self.col}, Mine={self.is_mine}, Flagged={self.is_flagged}, Unsure={self.is_unsure})"
