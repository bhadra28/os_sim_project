import tkinter as tk
from tkinter import ttk
import numpy as np


from bankers import *
from page_rep import *
from diskscheduling import *
from processsynch import *


def fun():
    exec(open('diskscheduling.py').read())

def main():
    mainwindow = tk.Tk()
    mainwindow.title("OS Simulator")
    mainwindow.minsize(400, 300)

    frame = tk.Frame(mainwindow)
    frame.grid(row=1, column=0)
    bankers_btn = tk.Button(master=frame, text="Banker's Algorithm", command=getinputBankers)
    bankers_btn.pack()
    CreateToolTip(bankers_btn, text = 'Generates a single safe sequence\n'
                 'Requires matrix input. Press tab to go to next input field faster!')

    pagerep_btn = tk.Button(master=mainwindow, text="Page replacement methods", command=getinputPagerep)
    pagerep_btn.grid(row=3, column=0)
    CreateToolTip(pagerep_btn, text = 'Generates analysis of page replacement methods\n'
                 'Gives number of page faults and frame contents for FIFO, LRU and OPTIMAL.')

    disksched_btn = tk.Button(master=mainwindow, text="Disk Scheduling methods", command=diskSchedulingMain)
    disksched_btn.grid(row=5, column=0)
    CreateToolTip(disksched_btn, text = 'This is a simulation\n'
                 'Delay of 3 seconds to generate output')

    dinnerp = tk.Button(mainwindow, text="Dining Philosopher", command = dp)
    dinnerp.grid(row=7, column=0)
    CreateToolTip(dinnerp, text = 'This is a simulation\n'
                 'Delay of 3 seconds to generate output')
    

    mainwindow.mainloop()

if __name__ == "__main__":
    main()