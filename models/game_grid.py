import random
from models.cell import Cell
from typing import List, Set, Tuple

class GameGrid:
    """
    Represents the game grid

    :param rows: int - Number of rows in the grid.
    :param cols: int - Number of columns in the grid.
    :param mines: int - Number of mines to place on the grid.
    """
    def __init__(self, rows: int, cols: int, mines: int):
        self.__rows: int = rows
        self.__cols: int = cols
        self.__mines: int = mines
        self.__cell_list: List[List[Cell]] = [[Cell(row, col) for col in range(cols)] for row in range(rows)]  # 2D grid of cells
        self.__first_click: tuple[int, int] | None = None  # Track the first clicked cell

    @property
    def rows(self) -> int:
        return self.__rows

    @property
    def cols(self) -> int:
        return self.__cols

    @property
    def mines(self) -> int:
        return self.__mines

    @property
    def cell_list(self) -> List[List[Cell]]:
        return self.__cell_list

    @property
    def first_click(self) -> tuple[int, int] | None:
        return self.__first_click

    def _place_mines(self, first_click_row: int, first_click_col: int) -> None:
        """
        Place mines on the grid, ensuring the first clicked cell is not a bomb.

        :param first_click_row: int - Row index of the first clicked cell.
        :param first_click_col: int - Column index of the first clicked cell.
        """
        self.__first_click = (first_click_row, first_click_col)
        excluded_positions: Set[Tuple[int, int]] = {(first_click_row, first_click_col)}
        mine_positions = set()

        while len(mine_positions) < self.__mines:
            row = random.randint(0, self.__rows - 1)
            col = random.randint(0, self.__cols - 1)
            if (row, col) not in excluded_positions and (row, col) not in mine_positions:
                mine_positions.add((row, col))

        for row, col in mine_positions:
            self.__cell_list[row][col].is_mine = True

    def _calculate_adjacent_mines(self) -> None:
        """
        Calculate the number of adjacent mines for each cell in the grid.
        """
        for row in range(self.__rows):
            for col in range(self.__cols):
                if not self.__cell_list[row][col].is_mine:
                    self.__cell_list[row][col].adjacent_mines = self._count_adjacent_mines(row, col)

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
            if 0 <= r < self.__rows and 0 <= c < self.__cols and self.__cell_list[r][c].is_mine:
                count += 1
        return count