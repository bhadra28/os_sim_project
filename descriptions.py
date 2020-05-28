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
    tbox.insert(tk.INSERT, "Banker's algorithm is used to find a safe sequence of processes for a given set of processes,each with their own amounts of resources required and resources held. In general, Banker's algorithm cannot be used in in scheduling systems because it requires processes to declare all the resources they might need at runtime itself.\n\nRead more at : https://en.wikipedia.org/wiki/Banker%27s_algorithm")


    tbox.config(state='disabled')


def MemAlloDesc():
    root = tk.Tk()
    root.title("Memory Management")
    root.minsize(700, 600)

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
    tbox.insert(tk.INSERT, "\tMemory management is a form of resource management applied to computer \nmemory.The essential requirement of memory management is to provide ways to \ndynamically allocate portions of memory to programs at their request, and free it for reuse when no longer needed. This is critical to any advanced computer \nsystem where more than a single process might be underway at any time\n\n")
    tbox.insert(tk.INSERT, "For More informtion visit : https://en.wikipedia.org/wiki/Memory_management")

    tbox.config(state='disabled')



    root.mainloop()