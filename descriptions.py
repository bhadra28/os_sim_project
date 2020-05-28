import tkinter as tk

def bankers_desc():
    root = tk.Tk()
    root.title("Banker's Algorithm")
    root.minsize(600, 700)

    desc_frame = tk.Frame(root, background='gray')
    desc_frame.pack(padx=10, pady=10, fill='both', expand=tk.YES)

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    canvas = tk.Canvas(desc_frame, background='gray')
    canvas.pack(side=tk.LEFT, fill='both', expand=tk.YES)

    scrollbar = tk.Scrollbar(desc_frame, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill='y')

    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.bind('<Configure>', on_configure)


    frame = tk.Frame(canvas, background='gray')
    canvas.create_window((0,0), window=frame, anchor='nw')


    lbl = tk.Label(frame, text="Banker's Algorithm", font="-size 20", background='gray')
    lbl.pack()

    tbox = tk.Text(frame, background='gray', wrap=tk.WORD)
    tbox.pack()
    tbox.insert(tk.INSERT, "This project is submitted to Shashidhar sir, Anappa Sir, and \nAnkit Sir, of the Computer Science department of NITK, Surathkal, \nas part of the course requirements for CS255, Operating Systems\n\n")


    tbox.config(state='disabled')


def MemAlloDesc():
    root = tk.Tk()
    root.title("Memory Allocation Algorithms")
    root.minsize(600, 700)

    desc_frame = tk.Frame(root, background='gray')
    desc_frame.pack(padx=10, pady=10, fill='both', expand=tk.YES)

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    canvas = tk.Canvas(desc_frame, background='gray')
    canvas.pack(side=tk.LEFT, fill='both', expand=tk.YES)

    scrollbar = tk.Scrollbar(desc_frame, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill='y')

    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.bind('<Configure>', on_configure)


    frame = tk.Frame(canvas, background='gray')
    canvas.create_window((0,0), window=frame, anchor='nw')


    lbl = tk.Label(frame, text="Memory Allocation Algorithm", font="-size 20", background='gray')
    lbl.pack()

    tbox = tk.Text(frame, background='gray', wrap=tk.WORD)
    tbox.pack()
    tbox.insert(tk.INSERT, "This project is submitted to Shashidhar sir, Anappa Sir, and \nAnkit Sir, of the Computer Science department of NITK, Surathkal, \nas part of the course requirements for CS255, Operating Systems\n\n")


    tbox.config(state='disabled')



    root.mainloop()