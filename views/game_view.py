import customtkinter as ctk
from typing import Callable
from constants import Difficulty

class GameView(ctk.CTk):
    """
    Represents the graphical user interface for the Minesweeper game.
    """
    def __init__(self) -> None:
        super().__init__()
        self.title("Minesweeper")
        self.resizable(False, False)
        self.grid_buttons = []  # 2D list
        self.timer_value = 0
        self.timer_running = False
        self.flags_left = 0
        self.difficulty = Difficulty.EASY

        # Create main layout containers
        self.menu_frame = ctk.CTkFrame(self, height=150)
        self.menu_frame.pack(fill="x", side="top", pady=10)

        self.grid_frame = ctk.CTkFrame(self)
        self.grid_frame.pack(fill="both", expand=True, side="top")

        # Configure menu_frame grid layout
        self.menu_frame.columnconfigure(0, weight=1)
        self.menu_frame.columnconfigure(1, weight=1)
        self.menu_frame.columnconfigure(2, weight=1)
        self.menu_frame.columnconfigure(3, weight=0)

        # Initialize menu widgets
        self.flags_label = ctk.CTkLabel(self.menu_frame, text=f"{self.flags_left}")
        self.flags_label.grid(row=0, column=0, padx=10, sticky="ew")

        self.reset_button = ctk.CTkButton(
            self.menu_frame, text="🔄", command=None, width=40, font=("Arial", 22, "bold")
        )  # Set later in create_menu
        self.reset_button.grid(row=0, column=1, padx=10, sticky="ew")

        self.timer_label = ctk.CTkLabel(self.menu_frame, text=f"{self.timer_value}")
        self.timer_label.grid(row=0, column=2, padx=10, sticky="ew")

        self.difficulty_menu = ctk.CTkOptionMenu(
            self.menu_frame,
            values=[d.name for d in Difficulty],
            command=None,  # Set later in create_menu
            width=100
        )
        self.difficulty_menu.set(self.difficulty.name)
        self.difficulty_menu.grid(row=0, column=3, padx=10, sticky="ew")

    def clear_view(self) -> None:
        """
        Clear all elements from the grid frame and reset the grid buttons.
        """
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        self.grid_buttons.clear()

    def create_menu(self, reset_game: Callable[[Difficulty], None]) -> None:
        """
        Create the menu interface with flags, difficulty selection, reset button, and timer.

        :param reset_game: Callable[[Difficulty], None] - Callback function to reset the game.
        """
        self.difficulty_menu.configure(
            command=lambda difficulty: self._update_difficulty_and_reset(difficulty, reset_game)
        )
        self.reset_button.configure(command=lambda: reset_game(self.difficulty))  # Pass current difficulty
        self.flags_label.configure(text=f"{self.flags_left}")

    def _update_difficulty_and_reset(self, difficulty: str, reset_game: Callable[[Difficulty], None]) -> None:
        """
        Update the difficulty and reset the game.

        :param difficulty: str - The new difficulty selected from the menu.
        :param reset_game: Callable[[Difficulty], None] - Callback function to reset the game.
        """
        self.difficulty = Difficulty[difficulty]
        reset_game(self.difficulty)

    def create_board(self, rows: int, cols: int, click_handler: Callable[[int, int], None], right_click_handler: Callable[[int, int], None]) -> None:
        """
        Create the game board with buttons for each cell.

        :param rows: int - Number of rows in the grid.
        :param cols: int - Number of columns in the grid.
        :param click_handler: Callable[[int, int], None] - Function to handle left-click events.
        :param right_click_handler: Callable[[int, int], None] - Function to handle right-click events.
        """
        self.grid_buttons = [[None for _ in range(cols)] for _ in range(rows)]  # Initialize 2D list
        for row in range(rows):
            for col in range(cols):
                button = ctk.CTkButton(
                    self.grid_frame,
                    text="",
                    width=32,
                    height=32,
                    fg_color="#c0c0c0",
                    hover_color="#d9d9d9",
                    text_color="#808080",
                    corner_radius=0,
                    border_width=3,
                    border_color="#a6a6a6",
                    command=lambda r=row, c=col: click_handler(r, c)
                )
                button.bind("<Button-3>", lambda event, r=row, c=col: right_click_handler(r, c))
                button.grid(row=row, column=col, padx=1, pady=1)
                self.grid_buttons[row][col] = button  # Store button in 2D list

    def update_cell(self, row: int, col: int, text: str, is_revealed: bool = False, is_mine = False, right_click_handler: Callable[[int, int], None] = None) -> None:
        """
        Update the appearance of a cell on the game board.

        :param row: int - Row index of the cell.
        :param col: int - Column index of the cell.
        :param text: str - Text to display on the cell.
        :param is_revealed: bool - Whether the cell is revealed.
        :param right_click_handler: Callable[[int, int], None] - Function to handle right-click events.
        """
        button = self.grid_buttons[row][col]

        if is_revealed:
            # Ensure text is treated as a string
            text = str(text)

            # Determine text color based on the text value
            if text.isdigit() and 1 <= int(text) <= 8:
                red_intensity = int(255 - (int(text) - 1) * (255 / 7))  # Gradation from light red to dark red
                text_color = f"#{red_intensity:02x}0000"  # Convert to hex color
            else:
                text_color="#8d8d8d"

            button.configure(
                text="",
                state="disabled",
                fg_color=("gray80", "gray20"),  # (Dark mode, Light mode)
                border_width=0
            )

            # Add a label inside the button to control the text color
            if is_mine == False:
                label = ctk.CTkLabel(
                    button,
                    text=text,
                    text_color=text_color,
                    fg_color=("gray80", "gray20"),
                    font=("Arial", 14, "bold")
                )
            else: 
                label = ctk.CTkLabel(
                    button,
                    text=text,
                    text_color=text_color,
                    fg_color=("#8B0000"),
                    font=("Arial", 14, "bold")
                )
            label.place(relx=0.5, rely=0.5, anchor="center")
        else:
            button.configure(
                text=text,
                font=("Arial", 14, "bold")
            )
        # Re-bind the method so that the new button text is also bound by it
        if right_click_handler:
            button.unbind("<Button-3>")
            button.bind("<Button-3>", lambda event: right_click_handler(row, col))

    def end_game_message(self, message: str) -> None:
        """
        Display an end game message.

        :param message: str - The message to display.
        """
        game_over_label = ctk.CTkLabel(self.grid_frame, text=message, font=("Arial", 24))
        game_over_label.grid(row=0, column=0, rowspan=len(self.grid_buttons), columnspan=len(self.grid_buttons[0]), pady=10)

    def increment_timer(self) -> None:
        """
        Start the timer and update the timer label every second.
        """
        if self.timer_running:
            self.timer_value += 1
            self.timer_label.configure(text=f"Timer: {self.timer_value:03d}")
            self.after(1000, self.increment_timer)

    def reset_timer(self) -> None:
        """
        Reset the timer to 0 and stop it.
        """
        self.timer_running = False
        self.timer_value = 0
        self.timer_label.configure(text=f"Timer: {self.timer_value:03d}")