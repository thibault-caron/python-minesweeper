import tkinter as tk
import configure as cfg
import emoji
import random
from cell import Cell

class StartBoard:
    def __init__(self, parent, rows, cols):
        self.parent = parent
        self.rows = rows
        self.cols = cols
        self.num_mines = 0
        self.cells = []
        self.create_cells()

    def create_cells(self):
        """create the grid of cells"""
        for row in range(self.rows):
            row_cells = []
            for col in range(self.cols):
                # create one cell
                cell = Cell(location=(row, col))
                cell.create_button(self.parent)
                cell.cell_button.grid(row=row, column=col)
                row_cells.append(cell)
            self.cells.append(row_cells) 

    def display_grid(self):
        """create the graphique grid"""
        




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