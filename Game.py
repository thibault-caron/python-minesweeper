import tkinter as tk
import configure as cfg

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
        self.create_grid()



    def get_level_data(self):
        """return the informations (rows, cols, num_mines) for the level"""
        level_data = self.level(self.current_level)
        return level_data

    def create_screen(self):
        """create the game screen"""
        # the screen size is dynamically based on the grid size
        cell_size = 30
        width = self.cols * cell_size + 50
        height = self.rows * cell_size + 500
        self.root.geometry(f"{width}x{height}")

        self.root.configure(bg = cfg.BACKGROUNG_COLOR)
        self.root.resizable(False, False)



    def refresh_game(self):
        pass

    def refresh_button(self):
        """"""
        pass

    def timer(self):
        pass

    def display_time(self):
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

    def display_num_flag_left(self):
        pass


    def run(self):
        """start the game loop"""
        self.root.mainloop()

if __name__ == "__main__":
    game1 = Game()
    game1.run()

    