from utils import *
from cell import Cell

root = create_window()

#load frames
top_frame(root)
center_frame(root)

class Grid:
    def __init__(self, center_frame, x, y):
        self.x = x
        self.y = y
        self.cells = []
        
        
    def create_grid(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = Cell(x, y)
                cell.create_button(center_frame)
                cell.cell_button_object.grid(
                    column=x,
                    row=y,
                    )

        cell = Cell()
        cell.cell_button_object(center_frame)
        cell.cell_button_object.grid(
            column=x,
            row=x,
            )