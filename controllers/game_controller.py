from models.game_grid import GameGrid
from views.game_view import GameView
from settings.difficulty import Difficulty

class GameController:
    def __init__(self, view: GameView) -> None:
        """
        Initialize the game controller.

        :param view: GameView - The game view instance.
        """
        self.view = view
        self.board = None
        self.is_revealing_mines = False

    def initialize_game(self, difficulty: Difficulty) -> None:
        """
        Initialize or reset the game with the specified difficulty.

        :param difficulty: Difficulty - Difficulty level to initialize or reset to.
        """
        self.is_revealing_mines = False  # Stop mine reveal if launched right after game_over
        self.view.reset_timer()
        self.view.clear_view()

        rows, cols, mines = difficulty.get_settings()
        self.board = GameGrid(rows, cols, mines)
        self.view.flags_left = mines
        self.view.difficulty = difficulty

        # Pass the initialize_game method as reset_game to create_menu
        self.view.create_menu(self.initialize_game)

        self.view.create_board(rows, cols, self.handle_cell_click, self.handle_cell_right_click)

    def _start_game(self, row: int, col: int) -> None:
        """
        Start the game by placing mines and calculating adjacent mines.

        :param row: int - Row index of the first clicked cell.
        :param col: int - Column index of the first clicked cell.
        """
        self.view.timer_running = True
        self.view.increment_timer()  # Start timer
        self.board._place_mines(row, col)
        self.board._calculate_adjacent_mines()

    def handle_cell_click(self, row: int, col: int) -> None:
        """
        Handle a left-click event on a cell.

        :param row: int - Row index of the clicked cell.
        :param col: int - Column index of the clicked cell.
        """
        if not self.view.timer_running and self.view.timer_value == 0:
            self._start_game(row, col)

        cell = self.board.cell_list[row][col]
        if cell.is_flagged or cell.is_unsure:
            return

        if cell.is_mine:
            self._trigger_game_over(row, col)
        else:
            self.reveal_cells(row, col)
            self.check_win_condition()

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
            self.view.update_cell(row, col, "?", right_click_handler=self.handle_cell_right_click)
        elif cell.is_unsure:
            cell.is_unsure = False
            self.view.update_cell(row, col, "")
        else:
            cell.is_flagged = True
            self.view.flags_left -= 1
            self.view.update_cell(row, col, "🚩", right_click_handler=self.handle_cell_right_click)

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

    def _trigger_game_over(self, row: int, col: int) -> None:
        """
        Trigger game over logic when a mine is clicked.

        :param row: int - Row index of the clicked mine.
        :param col: int - Column index of the clicked mine.
        """
        self.is_revealing_mines = True
        mine_positions = [
            (r, c) for r in range(self.board.rows) for c in range(self.board.cols)
            if self.board.cell_list[r][c].is_mine and (r, c) != (row, col)
        ]
        delay = 200 // self.view.difficulty.value
        self._reveal_mines_with_delay([(row, col)] + mine_positions, delay)
        self.view.timer_running = False
        self.handle_game_end("You are a looser!")

    def _reveal_mines_with_delay(self, bomb_positions: list[tuple[int, int]], delay: int = 200) -> None:
        """
        Reveal bomb cells one by one with a delay.

        :param bomb_positions: list[tuple[int, int]] - List of bomb cell positions.
        :param delay: int - Delay in milliseconds between revealing each bomb.
        """
        if not bomb_positions or not self.is_revealing_mines:
            self.is_revealing_mines = False
            return
        
        delay = int(delay * 0.99)

        row, col = bomb_positions.pop(0)
        self.view.update_cell(row, col, "💣", is_revealed=True, is_mine=True)
        self.view.after(delay, lambda: self._reveal_mines_with_delay(bomb_positions, delay))

    def handle_game_end(self, message: str) -> None:
        """
        Handle game over logic by disabling all buttons and unbinding events.

        :param message: str - The game over message to display.
        :param mine_bg_color: str - Background color for revealed mines.
        """
        for row in self.view.grid_buttons:
            for button in row:
                button.configure(state="disabled")
                button.unbind("<Button-3>")
        self.view.end_game_message(message)

    def check_win_condition(self) -> None:
        """
        Check if the player has won the game.
        """
        for row in self.board.cell_list:
            for cell in row:
                if not cell.is_mine and not cell.is_revealed:
                    return
        self.view.timer_running = False
        self.handle_game_end("You are the best!!")