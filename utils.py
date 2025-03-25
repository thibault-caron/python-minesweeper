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
    return (WIDTH/100) * percentage

def top_frame(root):
    top_frame = tk.Frame(root, bg="lightgrey")
    top_frame.place(width = width_prctg(90), height = height_prctg(10), x = width_prctg(5), y = height_prctg(5))
    return top_frame

def center_frame(root):
    center_frame = tk.Frame(root, bg="black")
    center_frame.place(width = width_prctg(90), height = height_prctg(80), x = width_prctg(5), y = height_prctg(15))
    return center_frame