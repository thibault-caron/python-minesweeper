from utils import *
from cell import Cell

root = create_window()

#load frames
top_frame(root)
center_frame(root)

class Grid:
    all = []
    def __init__(self, center_frame):
        Grid.all.append(self)
        
        
    def create_grid(self):
        for x in range(GRID_SIZE):
            for y in range(GRID_SIZE):
                cell = Cell(x, y)
                cell.create_button(center_frame)
                cell.cell_button_object.grid(
                    column=x,
                    row=y,
                    )