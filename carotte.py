import tkinter as tk
import configure as cfg
import random # attention : importer que ce ce qui est nécessaire pour ne pas surcharger le programme
from enum import Enum
import emoji
from game import Game

class CellState(Enum):
    """Enum for cell state"""
    QUESTION_MARK = -3
    FLAG = -2
    UNKNOW = -1
    EMPTY = 0 
    ONE_ADJ_BOMB = 1
    TWO_ADJ_BOMB = 2
    THREE_ADJ_BOMB = 3
    FOUR_ADJ_BOMB = 4
    FIVE_ADJ_BOMB = 5
    SIX_ADJ_BOMB = 6
    SEVEN_ADJ_BOMB = 7
    EIGHT_ADJ_BOMB = 8  


class Cell:
    # all = [] a quoi ca sert ? c'est quoi?
    def __init__(self, location):
        self.location = location # (row, col)
        self.cell_button = None
        self.is_mine = False
        self.state = CellState.UNKNOW


    def create_button(self, parent):
        """create a button"""
        self.cell_button = tk.Button(
            parent,
            bg=cfg.BUTTON_COLOR)
        self.cell_button.bind("<Button-1>", self.left_click_action)
        self.cell_button.bind("<Button-3>", self.right_click_action)

    def surrounded_mines(self):
        # compte les mines alentour, a voir si cette méthode reste la 
        pass

    def unknow_button(self, event):
        """remove the text from the button"""
        self.cell_button.configure(text="")
        self.state = CellState.UNKNOW
    
    def show_mine(self, event):
        """change the appearance of the button to show a mine and disable interactions"""
        self.cell_button.configure(
            text = f"{emoji.emojize(":bomb:")}",
            font = ("Helvetica", 10),
            bg = "red",
            state = "disabled",
        )

        self.cell_button.unbind("<Button-1>")
        self.cell_button.unbind("<Button-3>") 

        
    def show_number(self, event):
        """turn the button into label and show the number of adjacent bombs if any"""
        self.cell_button.destroy()
        self.cell_label = tk.Label(
            self.location,

        )

        self.cell_label.grid(row=self.cell_button.grid_info()["row"], column=self.cell_button.grid_info()["column"])
    

    def show_flag(self, event):
        """show the flag"""
        self.cell_button.configure(
            text= f"{emoji.emojize(":triangular_flag:")}",
            font=("Helvitica", 10),
            bg = "green"
            )
        self.state = CellState.FLAG

    def show_question_mark(self, event):
        """show the question mark"""
        self.cell_button.configure(
            text = f"{emoji.emojize(":red_question_mark:")}",
            font=("Helvitica", 10),
            bg = "yellow"
        )
        self.state = CellState.QUESTION_MARK

    def left_click_action(self, event):
        """actions for a left click"""
        match self.state:
            case CellState.FLAG | CellState.QUESTION_MARK:
                pass # commande pour qu'il ne se passe rien ==== .unbind()
            case CellState.UNKNOW:
                if self.is_mine == True:
                    # récupérer toute les cellules qui contiennent des bombes et leur appliquer show_mine
                    #fin de partie
                    self.show_mine


    def right_click_action(self, event):
        """actions for a right click"""
        match self.state:
            case CellState.UNKNOW:
                self.show_flag(event) #ATTENTION, faire un .unbind()!!!!! du click gauche sur le bouton!!!!
                self.state = CellState.FLAG
            case CellState.FLAG:
                self.show_question_mark(event)
                self.state = CellState.QUESTION_MARK
            case CellState.QUESTION_MARK:
                self.unknow_button(event)
                self.state = CellState.UNKNOW



# random.sample pour le mines aléatoire?
# pour rechercher les bombes autour d'un case, partir des coordonnées dans la matrice et retirer ou ajouter 1 à row ou col!!
# methode get_cell_by_axis et surrounded_cells qui retour un liste en fonction de get_cell_by_axis
# détruir composants? tkinter a voir.