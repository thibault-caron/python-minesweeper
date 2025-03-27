import tkinter as tk
import configure as cfg
from Grid import Grid
import emoji

class Game:
    def __init__(self):
        """initialize the game"""
        self.root = tk.Tk()
        self.root.title("Mines weeper") 

        self.current_level = 1 # default level
        level_data = self.level(self.current_level) # get the level data

        # initialize attributs from level_data
        self.rows = level_data["row"]
        self.cols = level_data["col"]
        self.num_mines = level_data["mines"]

        

        self.create_screen()



    def get_level_data(self):
        """return the informations (rows, cols, num_mines) for the level"""
        level_data = self.level(self.current_level)
        return level_data

    def create_screen(self):
        """create the game screen"""
        # the screen size is dynamically based on the grid size
        cell_size = 30
        screen_width = self.cols * cell_size + 50
        screen_height = self.rows * cell_size + 500
        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.configure(bg = cfg.BACKGROUNG_COLOR)
        self.root.resizable(False, False)

        # create two frame to organise the screen game
        top_frame = tk.Frame(
            self.root, 
            bg = "red",
            width = screen_width,
            height = 450
        )
        top_frame.place(x=0, y=0)

        bottom_frame = tk.Frame(
            self.root, 
            bg = "green",
            width = screen_width,
            height = screen_height - 450
        )
        bottom_frame.place(x=0, y=450)

        # create the button to refresh the game 
        refresh_button = tk.Button(
            top_frame,
            bg = "blue",
            text = f"{emoji.emojize(":slightly_smiling_face:")}",  #	:face_with_crossed-out_eyes:  /  	:smiling_face_with_sunglasses: 
            width=3,
            height=1
            command=self.refresh_game
            )
        refresh_button.place(x=((screen_width-50)//2), y=300)

        # create the label to display the number of flags
        flags_label = tk.Label(
            top_frame,
            text=f"FLAGS : {self.num_mines}"
            font=("Helvetica", 20)
        )
        flags_label.place(x=25, y=25)

        # create the menu to choose the level

        # create the label to display the timer

        # display the grid
        self.create_grid(bottom_frame)



    def create_grid(self, parent):
        """create and display grid in the bottom frame"""
        grid = Grid(parent, self.rows, self.cols)




    def refresh_game(self):
        """reset the game"""
        for widget in 



    def timer(self):
        pass


    def level(self, level):
        """return the level of the game : the size of the grid and the number of mines"""
        levels = {
            1 : {"row": 9, "col": 9, "mines": 10},
            2 : {"row": 16, "col": 16, "mines": 40},
            3 : {"row": 16, "col": 30, "mines": 99},
        }
        match level:
            case 1:
                return levels[1]
            case 2:
                return levels[2]
            case 3:
                return levels[3]
            case _:
                return "invalid level"
            
    def level_choise(self):
        pass


    def run(self):
        """start the game loop"""
        self.root.mainloop()

if __name__ == "__main__":
    game1 = Game()
    game1.run()

    