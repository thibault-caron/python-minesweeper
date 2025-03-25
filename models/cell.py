class Cell:
    def __init__(self, row: int, col: int):
        self.row: int = row
        self.col: int = col
        self.is_mine: bool = False
        self.is_revealed: bool = False
        self.is_flagged: bool = False
        self.is_unsure: bool = False
        self.adjacent_mines: int = 0

    def __repr__(self) -> str:
        return f"Cell({self.row}, {self.col}, Mine={self.is_mine}, Flagged={self.is_flagged}, Unsure={self.is_unsure})"
