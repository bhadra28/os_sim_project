import tkinter as tk
from tkinter import ttk
import numpy as np

def getinputBankers():
    input_win = tk.Tk()
    input_win.title("Banker's Algorithm Inputs")
    frame_0_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_0.grid(row=0, column=0)
    n_proc_lbl = tk.Label(master=frame_0_0, text="Number of processes")
    n_proc_lbl.pack()
    
    frame_1_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_0.grid(row=1, column=0)
    n_res_lbl = tk.Label(master=frame_1_0, text="Number of resources")
    n_res_lbl.pack()

    frame_0_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_1.grid(row=0, column=1)
    n_proc_entry = tk.Entry(master=frame_0_1)
    n_proc_entry.pack()

    frame_1_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_1.grid(row=1, column=1)
    n_res_entry = tk.Entry(master=frame_1_1)
    n_res_entry.pack()

    def submit():
        r = int(n_proc_entry.get())
        c = int(n_res_entry.get())

        input_win.destroy()
        bankers_input_mat(r, c)
    
    frame_2_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_2_1.grid(row=2, column=1)
    submit_btn = tk.Button(master=frame_2_1, text="Submit", command=submit)
    submit_btn.pack()

    input_win.mainloop()

def bankers(matrix, available, r, c):
    alloc = matrix[0:r, 0:c]
    maxi = matrix[0:r, c:2*c]
    need = maxi - alloc
    work = available
    finished = [False]*r
    seq = []
    check = True

    ans = True
    
    while(len(seq)<r):
        check = False
        print(len(seq))

        print("need")
        print(need)

        print("available")
        print(work)

        for i in range(r):
            if finished[i]==False and (need[i, :] <= work).all():
                seq.append(i)
                work+=alloc[i, :]
                finished[i]=True
                check = True
                print("Worked on sequence " + str(i))
                break

        if(check == False):
            break
    
    text = ""

    if len(seq) != r:
        ans=False
    else:
        ans=True
    
    print(text)
    bankers_win = tk.Tk()
    bankers_win.title("Banker's Algorithm Output")
    bankers_win.minsize(400, 300)
    frame = tk.Frame(master=bankers_win)



    if ans:
        res_lbl = tk.Label(frame, text="A valid sequence was found!", background='green', foreground='white')
        res_lbl.place(relx=.5, rely=.5, anchor="center")
        res_lbl.pack()

        text = "P" + " P".join(map(str, seq))

        seq_lbl = tk.Label(frame, text=text)
        seq_lbl.pack()
    else:
        res_lbl = tk.Label(frame, text="No valid sequence was found.", background='red', foreground='white')
        res_lbl.pack()


    
    
    frame.pack()

    quit_btn = tk.Button(master=bankers_win, text="Close", command=bankers_win.destroy)
    quit_btn.pack()

    bankers_win.mainloop()


def bankers_input_mat(r, c):
    window = tk.Tk()
    window.title("Banker's Algorithm Input")
    entryobj = []
    free = []   

    frame = tk.Frame(window, borderwidth=1)
    frame.grid(row=0, column=1, columnspan=c)
    lbl = tk.Label(master=frame, text="Resources Allocated")
    lbl.pack()

    frame = tk.Frame(window, borderwidth=1)
    val=0
    if c==1:
        val = 2
    else:
        val = int(3*c/2)
    frame.grid(row=0, column=val, columnspan=c)
    lbl = tk.Label(master=frame, text="Maximum Resources needed")
    lbl.pack()

    for i in range(r):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=i+2, column=0)
        lbl = tk.Label(master=frame, text="Process {}".format(i))
        lbl.pack()

    for i in range(c):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=1, column=i+1)
        lbl = tk.Label(master=frame, text="R{}".format(i))
        lbl.pack()

    for i in range(c):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=1, column=c+i+1)
        lbl = tk.Label(master=frame, text="R{}".format(i))
        lbl.pack()

    
    for i in range(r):
        for j in range(2*c):
            frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
            frame.grid(row=i+2, column=j+1, padx=5, pady=5)
            entry = tk.Entry(frame, width=5)
            entryobj.append(entry)
            entry.pack()


    frame = tk.Frame(window, borderwidth=1)
    frame.grid(row=r+3, column=0)
    lbl = tk.Label(master=frame, text="Initial Free resource")
    lbl.pack()

    for i in range(c):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=r+3, column=i+1)
        entry = tk.Entry(frame, width=5)
        free.append(entry)
        entry.pack()
    

    def takesum():
        matrix = []
        for obj in entryobj:
            temp = obj.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            matrix.append(temp)

        start = []
        for item in free:
            temp = item.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            start.append(temp)

        matrix = np.array(matrix).reshape(r, 2*c)
        window.destroy()

        bankers(matrix, start, r, c)


    submitspace = tk.Frame(master=window, borderwidth=1)
    submitspace.grid(row=r+4, column=1)

    quitspace = tk.Frame(master=window, borderwidth=1 )
    quitspace.grid(row=r+4, column=0)

    quit_btn = tk.Button(master=quitspace, text="Quit", command = window.destroy)
    quit_btn.pack()

    submit_btn = tk.Button(master=submitspace, text="Submit", command=takesum)
    submit_btn.pack()

    window.mainloop()
