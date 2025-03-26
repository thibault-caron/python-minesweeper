from models.game_grid import GameGrid
from views.game_view import GameView
from constants import Difficulty, difficulty_settings
from typing import Optional

class GameController:
    def __init__(self, view: GameView) -> None:
        """
        Initialize the game controller.

        :param view: GameView - The game view instance.
        """
        self.view = view
        self.board = None

    def initialize_game(self, difficulty: Optional[Difficulty] = None) -> None:
        """
        Initialize or reset the game with the specified difficulty.

        :param difficulty: Optional[Difficulty] - Difficulty level to initialize or reset to.
                           Defaults to the current difficulty.
        """
        if difficulty is None:
            difficulty = self.view.difficulty

        self.view.reset_timer()
        self.view.clear_view()

        rows, cols, mines = difficulty_settings[difficulty]  # imported from constants.py
        self.board = GameGrid(rows, cols, mines)
        self.view.flags_left = mines
        self.view.difficulty = difficulty
        self.view.create_menu(self.initialize_game)
        self.view.create_board(rows, cols, self.handle_cell_click, self.handle_cell_right_click)

    def handle_cell_click(self, row: int, col: int) -> None:
        """
        Handle a left-click event on a cell.

        :param row: int - Row index of the clicked cell.
        :param col: int - Column index of the clicked cell.
        """
        if not self.view.timer_running:
            self.view.timer_running = True
            self.view.increment_timer()  # Start the timer
            self.board._place_mines(row, col)
            self.board._calculate_adjacent_mines()
        cell = self.board.cell_list[row][col]
        if cell.is_flagged or cell.is_unsure: 
            return
        if cell.is_mine:
            mine_positions = [
                (r, c) for r in range(self.board.rows) for c in range(self.board.cols)
                if self.board.cell_list[r][c].is_mine and (r, c) != (row, col)
            ]  # list excluding the clicked mine cell
            self._reveal_bombs_with_delay([(row, col)] + mine_positions)  # "+" concatenates both into one tuple list
            self.view.timer_running = False
            self.view.show_game_over()
        else:
            self.reveal_cells(row, col)
            self.check_win_condition()

    def _reveal_bombs_with_delay(self, bomb_positions: list[tuple[int, int]], delay: int = 350) -> None:
        """
        Reveal bomb cells one by one with a delay.

        :param bomb_positions: list[tuple[int, int]] - List of bomb cell positions.
        :param delay: int - Delay in milliseconds between revealing each bomb.
        """
        if not bomb_positions:
            return
        row, col = bomb_positions.pop(0)
        self.view.update_cell(row, col, "💣", is_revealed=True)
        self.view.grid_buttons[row][col].configure(fg_color="#8B0000")  # Dark red background
        self.view.after(delay, lambda: self._reveal_bombs_with_delay(bomb_positions, delay))

    def check_win_condition(self) -> None:
        """
        Check if the player has won the game.
        """
        for row in self.board.cell_list:
            for cell in row:
                if not cell.is_mine and not cell.is_revealed:
                    return
        self.view.timer_running = False
        self.view.show_game_won() 

    def handle_cell_right_click(self, row: int, col: int) -> None:
        """
        Handle a right-click event on a cell.

        :param row: int - Row index of the clicked cell.
        :param col: int - Column index of the clicked cell.
        """
        cell = self.board.cell_list[row][col]
        if cell.is_revealed:
            return
        if cell.is_flagged:
            cell.is_flagged = False
            cell.is_unsure = True
            self.view.flags_left += 1
            self.view.update_cell(row, col, "?")
        elif cell.is_unsure:
            cell.is_unsure = False
            self.view.update_cell(row, col, "")
        else:
            cell.is_flagged = True
            self.view.flags_left -= 1
            self.view.update_cell(row, col, "🚩")
        self.view.flags_label.configure(text=f"{self.view.flags_left:02d}")

    def reveal_cells(self, row: int, col: int) -> None:
        """
        Reveal the cell at the specified position. If the cell has no adjacent mines,
        recursively reveal its neighbors.

        :param row: int - Row index of the cell to reveal.
        :param col: int - Column index of the cell to reveal.
        """
        cell = self.board.cell_list[row][col]
        if cell.is_revealed or cell.is_flagged:
            return

        cell.is_revealed = True
        self.view.update_cell(row, col, cell.adjacent_mines if cell.adjacent_mines > 0 else "", is_revealed=True)

        if cell.adjacent_mines == 0 and not cell.is_mine:
            directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < self.board.rows and 0 <= c < self.board.cols:
                    self.reveal_cells(r, c)