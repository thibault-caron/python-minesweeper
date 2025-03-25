import customtkinter as ctk
from typing import Callable
from models.menu import Menu

class GameView(ctk.CTk):
    """
    Represents the graphical user interface for the Minesweeper game.
    """
    def __init__(self) -> None:
        super().__init__()
        self.title("Minesweeper")
        self.grid_buttons = {}

        # Create main layout containers
        self.menu_frame = ctk.CTkFrame(self, height=150)
        self.menu_frame.pack(fill="x", side="top")

        self.grid_frame = ctk.CTkFrame(self)
        self.grid_frame.pack(fill="both", expand=True, side="top")

    def clear_view(self) -> None:
        """
        Clear all elements from the grid frame and reset the grid buttons.
        """
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.grid_buttons.clear()

    def create_menu(self, menu: Menu, reset_game: Callable[[str], None]) -> None:
        """
        Create the menu interface with flags, difficulty selection, reset button, and timer.

        :param menu: Menu - The menu model instance.
        :param reset_game: Callable[[str], None] - Callback function to reset the game.
        """
        self.clear_view()  
        self.flags_label = ctk.CTkLabel(self.menu_frame, text=f"Flags Left: {menu.flags_left}")
        self.flags_label.grid(row=0, column=0, padx=10)

        self.difficulty_menu = ctk.CTkOptionMenu(
            self.menu_frame,
            values=["easy", "medium", "hard"],
            command=lambda difficulty: self._on_difficulty_change(difficulty, reset_game)
        )
        self.difficulty_menu.set(menu.difficulty)
        self.difficulty_menu.grid(row=0, column=1, padx=10)

        self.reset_button = ctk.CTkButton(self.menu_frame, text="Reset", command=reset_game)
        self.reset_button.grid(row=0, column=3, padx=10)

        self.timer_label = ctk.CTkLabel(self.menu_frame, text=f"Timer: {menu.timer}")
        self.timer_label.grid(row=0, column=2, padx=10)

    def _on_difficulty_change(self, difficulty: str, reset_game: Callable[[str], None]) -> None:
        """
        Handle difficulty change events and reset the game with the selected difficulty.

        :param difficulty: str - The selected difficulty level.
        :param reset_game: Callable[[str], None] - Callback function to reset the game.
        """
        reset_game(difficulty)

    def update_menu(self, flags_left: int, timer: int) -> None:
        """
        Update the menu display with the current number of flags left and the timer value.

        :param flags_left: int - Number of flags left.
        :param timer: int - Current timer value.
        """
        self.flags_label.configure(text=f"Flags Left: {flags_left}")
        self.timer_label.configure(text=f"Timer: {timer}")

    def create_board(self, rows: int, cols: int, click_handler: Callable[[int, int], None], right_click_handler: Callable[[int, int], None]) -> None:
        """
        Create the game board with buttons for each cell.

        :param rows: int - Number of rows in the grid.
        :param cols: int - Number of columns in the grid.
        :param click_handler: Callable[[int, int], None] - Function to handle left-click events.
        :param right_click_handler: Callable[[int, int], None] - Function to handle right-click events.
        """
        for row in range(rows):
            for col in range(cols):
                button = ctk.CTkButton(
                    self.grid_frame, text="", width=40, height=40,
                    command=lambda r=row, c=col: click_handler(r, c)
                )
                button.bind("<Button-3>", lambda event, r=row, c=col: right_click_handler(r, c))  # Right-click binding
                button.grid(row=row, column=col, padx=2, pady=2)
                self.grid_buttons[(row, col)] = button

    def update_cell(self, row: int, col: int, text: str, is_revealed: bool = False) -> None:
        """
        Update the appearance of a cell on the game board.

        :param row: int - Row index of the cell.
        :param col: int - Column index of the cell.
        :param text: str - Text to display on the cell.
        :param is_revealed: bool - Whether the cell is revealed.
        """
        button = self.grid_buttons[(row, col)]
        if is_revealed:
            button.configure(
                text=text,
                state="disabled",
                fg_color=("gray20", "gray80")  # Dark mode: gray20, Light mode: gray80
            )
        else:
            button.configure(text=text)

    def show_game_over(self) -> None:
        """
        Display a game over message and disable all buttons on the board.
        """
        for button in self.grid_buttons.values():
            button.configure(state="disabled")
        game_over_label = ctk.CTkLabel(self.grid_frame, text="Game Over!", font=("Arial", 24))
        game_over_label.grid(row=0, column=0, columnspan=len(self.grid_buttons), pady=10)

    def show_game_won(self) -> None:
        """
        Display a game won message and disable all buttons on the board.
        """
        for button in self.grid_buttons.values():
            button.configure(state="disabled")
        game_won_label = ctk.CTkLabel(self.grid_frame, text="You Won!", font=("Arial", 24))
        game_won_label.grid(row=0, column=0, columnspan=len(self.grid_buttons), pady=10)
