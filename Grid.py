import tkinter as tk
import configure as cfg
import emoji
import random
from Cell import Cell

class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.num_mines = 0
        self.cells = []
        self.create_cells()

    def create_cells(self):
        """create tthe grid of cells"""
        pass

    def place_mines(self):
        """place mines randomly in the grid"""
        pass

    def get_cell(self, row, col):
        """return the cell at given position"""
        pass

    def reveal_all_mines(self):
        """reveal all mines in the grid"""
        pass

    def get_surrounging_cells(self, row, col):
        """return a list of surrounding cells"""