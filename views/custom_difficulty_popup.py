import customtkinter as ctk
from settings.difficulty import CustomDifficulty
from tkinter import messagebox

class CustomDifficultyPopup(ctk.CTkToplevel):
    """
    Popup window for entering custom difficulty settings.
    """
    def __init__(self, parent, on_submit):
        """
        Initialize the popup window.

        :param parent: The parent window.
        :param on_submit: Callback function to handle the submitted settings.
        """
        super().__init__(parent)
        self.title("Custom Difficulty")
        self.geometry("300x280")
        self.resizable(False, False)
        self.on_submit = on_submit

        # Make the popup appear in front of the parent window
        self.transient(parent)
        self.grab_set()  # Make the popup modal
        self.focus_force()  # Focus on the popup

        # Input fields
        self.row_label = ctk.CTkLabel(self, 
            text=f"Rows ({CustomDifficulty.MIN_ROWS}-{CustomDifficulty.MAX_ROWS}):"
        )
        self.row_label.pack(pady=5)
        self.row_entry = ctk.CTkEntry(self)
        self.row_entry.pack(pady=5)

        self.col_label = ctk.CTkLabel(self,
            text=f"Columns ({CustomDifficulty.MIN_COLS}-{CustomDifficulty.MAX_COLS}):"
        )
        self.col_label.pack(pady=5)
        self.col_entry = ctk.CTkEntry(self)
        self.col_entry.pack(pady=5)

        self.mine_label = ctk.CTkLabel(self, 
            text=f"Mines ({CustomDifficulty.MIN_MINES}-max):"
        )
        self.mine_label.pack(pady=5)
        self.mine_entry = ctk.CTkEntry(self)
        self.mine_entry.pack(pady=5)

        # Submit button
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self._handle_submit)
        self.submit_button.pack(pady=10)

    def _handle_submit(self):
        """
        Handle the submission of custom difficulty settings.
        """
        try:
            rows = int(self.row_entry.get())
            cols = int(self.col_entry.get())
            mines = int(self.mine_entry.get())

            # Validate settings
            CustomDifficulty.set_settings(rows, cols, mines)
            self.on_submit()  # Call the callback function
            self.destroy()  # Close the popup
        except ValueError as e:
            messagebox.showerror("Invalid Input", str(e))
        except Exception:
            messagebox.showerror("Error", "Please enter valid numbers for all fields.")
