import tkinter as tk
from tkinter import ttk
import numpy as np

from bankers import *


def main():
    mainwindow = tk.Tk()
    mainwindow.title("OS Simulator")
    mainwindow.minsize(400, 300)
    matdisplay_btn = tk.Button(master=mainwindow, text="Banker's Algorithm", command=getinputBankers)
    matdisplay_btn.pack()
    mainwindow.mainloop()

if __name__ == "__main__":
    main()