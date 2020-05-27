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
    frame.pack(padx=10, pady=10)
    bankers_btn = tk.Button(frame, text="Banker's Algorithm", command=getinputBankers)
    bankers_btn.pack()
    CreateToolTip(bankers_btn, text = 'Generates a single safe sequence\n'
                 'Requires matrix input. Press tab to go to next input field faster!')

    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    pagerep_btn = tk.Button(frame, text="Page replacement methods", command=getinputPagerep)
    pagerep_btn.grid(row=3, column=0)
    CreateToolTip(pagerep_btn, text = 'Generates analysis of page replacement methods\n'
                 'Gives number of page faults and frame contents for FIFO, LRU and OPTIMAL.')

    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    disksched_btn = tk.Button(frame, text="Disk Scheduling methods", command=diskSchedulingMain)
    disksched_btn.pack()
    CreateToolTip(disksched_btn, text = 'Implementation\n'
                 'Output is in textboxes')

    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    dinnerp = tk.Button(frame, text="Dining Philosopher", command = dp)
    dinnerp.pack()
    CreateToolTip(dinnerp, text = 'This is a simulation\n'
                 'Delay of 3 seconds to generate output'
                 'Simulates 5 philosophers in the dining philosophers problem')
    
    frame = tk.Frame(mainwindow)
    frame.pack(padx=10, pady=10)
    dinnerp = tk.Button(frame, text="Sleeping Barbers", command = sb)
    dinnerp.pack()
    CreateToolTip(dinnerp, text = 'This is a simulation\n'
                 'Delay of a few seconds to generate output'
                 'Simulates 50 customers and 3 barbers in the sleeping barbers problem')


    mainwindow.mainloop()

if __name__ == "__main__":
    main()