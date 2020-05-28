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
    root.mainloop()

def disk_desc():
    root = tk.Tk()
    root.title("Disc Scheduling Algorithms")
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


    lbl = tk.Label(frame, text="Disk Scheduling Algorithms", font="-size 20", background='gray')
    lbl.pack()

    tbox = tk.Text(frame, background='gray', wrap=tk.WORD)
    tbox.pack()
    tbox.insert(tk.INSERT, "Information stored on disk needs to be retrieved at a rate optimal for processing in CPU. With caches and buffers, there is no problem if the data is early, but we must ensure that disks are read efficiently so as to not be late. To this end, we have disk scheduling algorithms like \n\nShortest Seek Time First (https://en.wikipedia.org/wiki/Shortest_seek_first), \n\nSCAN (https://en.wikipedia.org/wiki/Elevator_algorithm), \n\nCircular SCAN (https://www.geeksforgeeks.org/c-scan-disk-scheduling-algorithm/), \n\nLOOK (https://en.wikipedia.org/wiki/LOOK_algorithm), and\n\nCLOOK (https://www.gatevidyalay.com/c-look-algorithm-disk-scheduling-algorithms/)")


    tbox.config(state='disabled')
    root.mainloop()

def proc_desc():
    root = tk.Tk()
    root.title("Process Scheduling Algorithms")
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


    lbl = tk.Label(frame, text="Process Scheduling Algorithms", font="-size 20", background='gray')
    lbl.pack()

    tbox = tk.Text(frame, background='gray', wrap=tk.WORD)
    tbox.pack()
    tbox.insert(tk.INSERT, "CPU Scheduling is a process of determining which process will own CPU for execution while another process is on hold. The main task of CPU scheduling is to make sure that whenever the CPU remains idle, the OS at least select one of the processes available in the ready queue for execution. The selection process will be carried out by the CPU scheduler. It selects one of the processes in memory that are ready for execution.\n\nRead more at : https://en.m.wikipedia.org/wiki/Scheduling_(computing)")


    tbox.config(state='disabled')


def MemAlloDesc():
    root = tk.Tk()
    root.title("Memory Management Algorithms")
    root.minsize(700, 700)

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


    lbl = tk.Label(frame, text="Memory Management Algorithms", font="-size 20", background='gray')
    lbl.pack()

    tbox = tk.Text(frame, background='gray', wrap=tk.WORD)
    tbox.pack()
    tbox.insert(tk.INSERT, "Memory management is a form of resource management applied to computer memory. \nThe essential requirement of memory management is to provide ways to dynamically \nallocate portions of memory to programs at their request, and free it \nfor reuse when no longer needed. This is critical to any advanced computer \nsystem where more than a single process might be underway at any time\n\nFor More Info : https://en.wikipedia.org/wiki/Memory_management")


    tbox.config(state='disabled')
    root.mainloop()
    
def page_rep_desc():
    root = tk.Tk()
    root.title("Page Replacement Algorithms")
    root.minsize(600, 700)

    desc_frame = tk.Frame(root, background='white')
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


    lbl = tk.Label(frame, text="Page Replacement Algorithms", font="-size 20", background='gray')
    lbl.pack()

    tbox = tk.Text(frame, background='gray', wrap=tk.WORD)
    tbox.pack()
    tbox.insert(tk.INSERT,"In a computer operating system that uses paging for virtual memory management, page replacement algorithms decide which memory pages to page out, sometimes called swap out, or write to disk, when a page of memory needs to be allocated. Page replacement happens when a requested page is not in memory (page fault) and a free page cannot be used to satisfy the allocation, either because there are none, or because the number of free pages is lower than some threshold.\n\n Read more at:\n https://en.wikipedia.org/wiki/Page_replacement_algorithm")


    tbox.config(state='disabled')
    
    root.mainloop()
