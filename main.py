from utils import *
from cell import Cell

root = create_window()
Cell.initialize_images()

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
    height = height_prctg(20),
    x = width_prctg(5),
    y = height_prctg(5)
    )

# initialize the center frame
center_frame = tk.Frame(root,
                        bg="black",
                        width = width_prctg(90),
                        height = height_prctg(70)
                        )
center_frame.place(
    x = width_prctg(5),
    y = height_prctg(20)
    )

Cell.center_frame = center_frame

# create the grid
for x in range(GRID_SIZE):
    for y in range(GRID_SIZE):
        cell = Cell(x, y)
        cell.create_button(center_frame)
        cell.cell_button_object.grid(
            column=x,
            row=y,
            sticky="nsew"
        )

# show counter label in top frame
Cell.counter_label(top_frame)
Cell.cell_counter_object.grid(
    column=0,
    row=0
    )

# Add the "New Game" button
new_game_btn = Cell.new_game_button(top_frame)
new_game_btn.grid(
    column=1,
    row=0,
    padx=width_prctg(4)
    )


# randomize the mines        
Cell.randomize_mine()


if __name__ == "__main__":
    main()
    # run the window
    root.mainloop()