from utils import *
from cell import Cell
# from grid import Grid

root = create_window()

def main():
    # game = Game()
    # game.mainloop()
    pass

center_frame = tk.Frame(root,
                        bg="black",
                        width = width_prctg(90),
                        height = height_prctg(80)
                        )
center_frame.place(
    x = width_prctg(5),
    y = height_prctg(15)
    )

for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        cell = Cell(x, y)
        cell.create_button(center_frame)
        cell.cell_button_object.grid(
            column=x, row=y,
            )

if __name__ == "__main__":
    main()
    # Grid.create_grid()
    # run the window
    root.mainloop()