import tkinter as tk
from utils import *

class Cell:
    all = []
    def __init__(self, x, y, is_mine = False):
        
        self.is_mine = is_mine
        self.cell_button_object = None
        
        self.x = x
        self.y = y
        
        # add the cell to the list of all cells
        Cell.all.append(self)
        
        
    def create_button(self, location):
        button = tk.Button(
                           location,
                           text = f"{self.x}, {self.y}",
                           bg = "grey",
                           width=12,
                           height=4,
                           )
        button.bind("<Button-1>", self.left_click)
        button.bind("<Button-3>", self.right_click)
        
        self.cell_button_object = button