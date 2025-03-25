import tkinter as tk
from utils import *
import random

class Cell:
    all = []
    cell_counter_object = None 
    cell_left = CELLS_COUNT       
    def __init__(self, x, y, is_mine = False):
        
        self.is_mine = is_mine
        self.is_revealed = False
        self.cell_button_object = None
        
        self.x = x
        self.y = y
        
        # add the cell to the list of all cells
        Cell.all.append(self)
        
        
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
        if self.is_mine:
            self.show_mine()
        else:
            if self.surronded_cells_mine_count == 0:
                for cell in self.get_surronded_cells:
                    cell.show_number()
            self.show_number()
            
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
            
        # Mark the cell as revealed
        self.is_revealed = True
            
    def show_mine(self):
        # A logic to show the mine and end the game showing a message box
        self.cell_button_object.destroy()
        self.cell_button_object = tk.Label(
            self.cell_button_object.master,
            text="X",
            bg="red",
            width=14,
            height=5,
            )
        self.cell_button_object.grid(
            column=self.x, row=self.y,
            sticky="nsew"
            )
        
    def right_click(self, event):
        print("right click")
    
    @staticmethod    
    def randomize_mine():
        picked_cells = random.sample(Cell.all, MINE_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
        print(picked_cells)
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"