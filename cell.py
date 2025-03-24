import tkinter as tk
from utils import *

class Cell:
    def __init__(self, x, y, is_mine = False):
        
        self.is_mine = is_mine
        self.cell_button_object = None
        
        self.x = x
        self.y = y

    def create_button(self, location):
        button = tk.Button(
                           location,
                           text = "",
                           bg = "grey",
                           width=12,
                           height=4,
                           )
        
        self.cell_button_object = button