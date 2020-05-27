import tkinter as tk
from tkinter import ttk
import numpy as np

from bankers import *
from page_rep import *


def main():
    mainwindow = tk.Tk()
    mainwindow.title("OS Simulator")
    mainwindow.minsize(400, 300)
    bankers_btn = tk.Button(master=mainwindow, text="Banker's Algorithm", command=getinputBankers)
    bankers_btn.pack()
    pagerep_btn = tk.Button(master=mainwindow, text="Page replacement methods", command=getinputPagerep)
    pagerep_btn.pack()
    mainwindow.mainloop()

if __name__ == "__main__":
    main()