from utils import *
from cell import Cell

root = create_window()

def main():
    # game = Game()
    # game.mainloop()
    pass


# initialize the top frame
top_frame = tk.Frame(
    root,
    bg="grey",
    relief="raised",
    borderwidth=10
    )
top_frame.place(
    width = width_prctg(44.5),
    height = height_prctg(10),
    x = width_prctg(5),
    y = height_prctg(5)
    )

# initialize the center frame
center_frame = tk.Frame(root,
                        bg="black",
                        width = width_prctg(90),
                        height = height_prctg(80)
                        )
center_frame.place(
    x = width_prctg(5),
    y = height_prctg(15)
    )

# create the grid
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        cell = Cell(x, y)
        cell.create_button(center_frame)
        cell.cell_button_object.grid(
            column=x, row=y,
        )


if __name__ == "__main__":
    main()
    # run the window
    root.mainloop()