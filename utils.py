import tkinter as tk
from settings import *

def create_window():
    # overriding the default window
    root = tk.Tk()
    root.title("Mine Sweeper")
    root.configure(bg="black")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(False, False)
    return root

def height_prctg(percentage):
    return (HEIGHT/100) * percentage

def width_prctg(percentage):
    return (HEIGHT/100) * percentage