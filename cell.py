import tkinter as tk
from utils import *
import random
from PIL import Image, ImageTk

class Cell:
    all = []
    cell_counter_object = None 
    cell_left = CELLS_COUNT
    
    flag_image = None
    question_image = None
    bomb_image = None
    game_message = None
    first_click = True
         
    def __init__(self, x, y, is_mine = False):
        
        self.is_mine = is_mine
        self.is_revealed = False
        self.is_flagged = False
        self.is_questioned = False
        
        self.cell_button_object = None
        
        self.x = x
        self.y = y
        
        # add the cell to the list of all cells
        Cell.all.append(self)
    
    @staticmethod
    def initialize_images():
        """Resizes and initializes images once Tkinter root exists."""
        if Cell.flag_image is None:
            img = Image.open("assets/icons/flag.png")  # Load image
            img = img.resize((30, 30), Image.Resampling.LANCZOS)  # Resize to 30x30 pixels
            Cell.flag_image = ImageTk.PhotoImage(img)  # Convert to Tkinter-compatible format
        
        if Cell.question_image is None:
            img = Image.open("assets/icons/question.png")
            img = img.resize((30, 30), Image.Resampling.LANCZOS)
            Cell.question_image = ImageTk.PhotoImage(img)
            
        if Cell.bomb_image is None:
            img = Image.open("assets/icons/bomb.png")
            img = img.resize((30, 30), Image.Resampling.LANCZOS)
            Cell.bomb_image = ImageTk.PhotoImage(img)
        
    def create_button(self, location):
        button = tk.Button(
                           location,
                           bg = "grey",
                           width=12,
                           height=4,
                           relief="raised",
                           borderwidth=8
                           )
        button.bind("<Button-1>", self.left_click)
        button.bind("<Button-3>", self.right_click)
        
        self.cell_button_object = button
    
    @staticmethod    
    def counter_label(location):
        counter = tk.Label(
            location,
            text=f"Left: {Cell.cell_left}",
            bg="black",
            fg="lime",
            font=("Retro gaming", 24),
            )
        Cell.cell_counter_object = counter
        
    def left_click(self, event):
        # wait for the first left click to randomize the mines
        if Cell.first_click:
            Cell.first_click = False
            Cell.randomize_mine(self)
        
        if self.is_mine:
            for cell in Cell.all:
                if cell.is_mine:
                    cell.show_mine()
                if isinstance(cell.cell_button_object, tk.Button):
                    cell.cell_button_object.configure(state="disabled")
                    cell.cell_button_object.unbind("<Button-1>")
                    cell.cell_button_object.unbind("<Button-3>")
            Cell.show_game_message("Game Over! You hit a mine!")
        else:
            if self.surronded_cells_mine_count == 0:
                for cell in self.get_surronded_cells:
                    cell.show_number()
            self.show_number()
            
    @staticmethod
    def show_game_message(message):
        """Displays a win or lose message on the screen."""
        if Cell.game_message:
            Cell.game_message.destroy()  # Remove previous message if any
        
        Cell.game_message = tk.Label(
            Cell.center_frame,
            text=message,
            font=("Retro Gaming", 24),
            bg="black",
            fg="red" if message == "Game Over! You hit a mine!" else "lime"
        )
        Cell.game_message.place(relx=0.5, rely=0.5, anchor="center")
            
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell   
    
    @property        
    def get_surronded_cells(self):
        # A logic to show the number of mines surrounding the cell
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    @property
    def surronded_cells_mine_count(self):
        count = 0
        for cell in self.get_surronded_cells:
            if cell.is_mine:
                count += 1
        return count
            
    def show_number(self):
        # create a counter for the number of cells left
        if not self.is_revealed:
            Cell.cell_left -= 1
            
            self.cell_button_object.destroy()
            self.cell_button_object = tk.Label(
                self.cell_button_object.master,
                text=self.surronded_cells_mine_count,
                bg="grey",
                width=14,
                height=5,
                )
            self.cell_button_object.grid(
                column=self.x, row=self.y,
                sticky="nsew"
                )
            if Cell.cell_counter_object:
                Cell.cell_counter_object.config(
                    text=f"Left: {Cell.cell_left}"
                    )
        # Check win condition
        self.win_condition()
        
        # Mark the cell as revealed
        self.is_revealed = True
            
    def show_mine(self):
        # A logic to show all mines and end the game with a message (refer to left_click method in is_mine condition)
        self.cell_button_object.destroy()
        self.cell_button_object = tk.Label(
            self.cell_button_object.master,
            image=Cell.bomb_image,
            compound="center",
            bg="red",
            width=14,
            height=5,
            )
        self.cell_button_object.grid(
            column=self.x, row=self.y,
            sticky="nsew"
            )
        
    def right_click(self, event):
            if not self.is_flagged and not self.is_questioned:
                self.cell_button_object.config(image=Cell.flag_image, compound="center")
                self.is_flagged = True
                
            elif self.is_flagged:
                self.cell_button_object.config(image=Cell.question_image, compound="center")
                self.is_flagged = False
                self.is_questioned = True
                
            elif self.is_questioned:
                empty_img = tk.PhotoImage()
                self.cell_button_object.config(image=empty_img)
                self.cell_button_object.image = empty_img
                self.is_questioned = False
                
    def win_condition(self):
        if Cell.cell_left == MINE_COUNT:
            for cell in Cell.all:
                if isinstance(cell.cell_button_object, tk.Button):
                    cell.cell_button_object.unbind("<Button-1>")
                    cell.cell_button_object.unbind("<Button-3>")
                    cell.cell_button_object.configure(state="disabled")
                    
            Cell.show_game_message("Congratulations! You won!")
    
    @staticmethod
    def new_game():
        """Resets the game by clearing the grid and generating new mines."""
        # Destroy all existing buttons
        for cell in Cell.all:
            if cell.cell_button_object:
                cell.cell_button_object.destroy()
                
        # destroy the message
        if Cell.game_message:
            Cell.game_message.destroy()
            Cell.game_message = None
        
        # Clear the cell list
        Cell.all.clear()
        
        # Reset first click to ensure mines are randomized on first move
        Cell.first_click = True
        
        # Reset the counter
        Cell.cell_left = CELLS_COUNT
        if Cell.cell_counter_object:
            Cell.cell_counter_object.config(text=f"Left: {Cell.cell_left}")
        
        # Recreate the grid
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = Cell(x, y)
                cell.create_button(Cell.center_frame)  # Create new buttons inside center_frame
                cell.cell_button_object.grid(column=x, row=y, sticky="nsew")

        # Randomize new mines
        Cell.randomize_mine()

    @staticmethod    
    def new_game_button(location):    
        start_button = tk.Button(
            location,
            text="Restart",
            bg="grey",
            fg="lime",
            font=("Retro gaming", 24),
            relief="raised",
            borderwidth=10,
            command=Cell.new_game
            )
        return start_button
    
    @staticmethod            
    def randomize_mine(first_clicked_cell):
        # randomize mine after first left click
        # Get all possible cells except the first clicked cell
        available_cells = [cell for cell in Cell.all if cell != first_clicked_cell]
        
        picked_cells = random.sample(available_cells, MINE_COUNT)
        
        if len(available_cells) < MINE_COUNT:
            raise ValueError("Not enough spaces to place mines!")
        
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        print(picked_cells)
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"