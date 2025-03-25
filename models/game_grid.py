import random
from models.cell import Cell
from typing import List

class GameGrid:
    """
    Represents the game grid

    :param rows: int - Number of rows in the grid.
    :param cols: int - Number of columns in the grid.
    :param mines: int - Number of mines to place on the grid.
    """
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows: int = rows
        self.cols: int = cols
        self.mines: int = mines
        self.cell_list: List[List[Cell]] = [[Cell(row, col) for col in range(cols)] for row in range(rows)]  # 2D grid of cells
        self.first_click: tuple[int, int] | None = None  # Track the first clicked cell

    def _place_mines(self, first_click_row: int, first_click_col: int) -> None:
        """
        Place mines on the grid, ensuring the first clicked cell is not a bomb.

        :param first_click_row: int - Row index of the first clicked cell.
        :param first_click_col: int - Column index of the first clicked cell.
        """
        self.first_click = (first_click_row, first_click_col)
        all_positions = [(r, c) for r in range(self.rows) for c in range(self.cols)]
        all_positions.remove(self.first_click)  # Exclude the first clicked cell
        mine_positions = random.sample(all_positions, self.mines)
        for row, col in mine_positions:
            self.cell_list[row][col].is_mine = True

    def _calculate_adjacent_mines(self) -> None:
        """
        Calculate the number of adjacent mines for each cell in the grid.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if not self.cell_list[row][col].is_mine:
                    self.cell_list[row][col].adjacent_mines = self._count_adjacent_mines(row, col)

    def _count_adjacent_mines(self, row: int, col: int) -> int:
        """
        Count the number of mines adjacent to a given cell.

        :param row: int - Row index of the cell.
        :param col: int - Column index of the cell.
        :return: int - Number of adjacent mines.
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        count = 0
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < self.rows and 0 <= c < self.cols and self.cell_list[r][c].is_mine:
                count += 1
        return count