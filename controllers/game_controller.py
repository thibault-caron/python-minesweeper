from models.game_grid import GameGrid
from models.menu import Menu

class GameController:
    def __init__(self, view):
        self.view = view
        self.board = None
        self.menu = None

    def start_game(self, difficulty="easy"):
        difficulty_settings = {
            "easy": (9, 9, 10),
            "medium": (16, 16, 40),
            "hard": (16, 30, 99)
        }
        rows, cols, mines = difficulty_settings[difficulty]
        self.board = GameGrid(rows, cols, mines)
        self.menu = Menu(mines, difficulty)
        self.view.create_menu(self.menu, self.reset_game)
        self.view.create_board(rows, cols, self.handle_cell_click, self.handle_cell_right_click)

    def reset_game(self, difficulty=None):
        if difficulty is None:
            difficulty = self.menu.difficulty  # Use the current difficulty if not provided
        self.menu.stop_timer()
        self.view.clear_view()  # Clear the view before resetting
        self.start_game(difficulty)

    def handle_cell_click(self, row, col):
        if self.menu.timer == 0:
            self.menu.start_timer() 
            self.board._place_mines(row, col)
            self.board._calculate_adjacent_mines()
        cell = self.board.cell_list[row][col]
        if cell.is_flagged or cell.is_unsure: 
            return
        if cell.is_mine:
            self.view.update_cell(row, col, "B", is_revealed=True)
            self.view.show_game_over()
        else:
            self.reveal_cells(row, col)
            self.check_win_condition()

    def check_win_condition(self):
        for row in self.board.cell_list:
            for cell in row:
                if not cell.is_mine and not cell.is_revealed:
                    return
        self.view.show_game_won() 

    def handle_cell_right_click(self, row, col):
        cell = self.board.cell_list[row][col]
        if cell.is_revealed:
            return
        if cell.is_flagged:
            cell.is_flagged = False
            cell.is_unsure = True
            self.menu.flags_left += 1
            self.view.update_cell(row, col, "?")
        elif cell.is_unsure:
            cell.is_unsure = False
            self.view.update_cell(row, col, "")
        else:
            cell.is_flagged = True
            self.menu.flags_left -= 1
            self.view.update_cell(row, col, "F")
        self.view.update_menu(self.menu.flags_left, self.menu.timer)

    def reveal_cells(self, row: int, col: int) -> None:
        """
        Reveal the cell at (row, col). If the cell has no adjacent mines, 
        recursively reveal its neighbors.
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