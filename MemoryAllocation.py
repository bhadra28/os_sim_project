import tkinter as tk

def main():
    mainwindow = tk.Tk()
    mainwindow.title("OS Simulator")
    mainwindow.minsize(400, 300)
    matdisplay_btn = tk.Button(master=mainwindow, text="Memory Allocation Algorithm", command=getinputMA)
    matdisplay_btn.pack()
    mainwindow.mainloop()
    
def getinputMA():
    input_win = tk.Tk()
    
    frame_0_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_0.grid(row=0, column=0)
    n_blk_lbl = tk.Label(master=frame_0_0, text="Number of Blocks")
    n_blk_lbl.pack()
    
    frame_1_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_0.grid(row=0, column=0)
    n_proc_lbl = tk.Label(master=frame_0_0, text="Number of processes")
    n_proc_lbl.pack()
    
    frame_0_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_1.grid(row=0, column=1)
    n_blk_entry = tk.Entry(master=frame_0_1)
    n_blk_entry.pack()

    frame_1_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_1.grid(row=1, column=1)
    n_proc_entry = tk.Entry(master=frame_1_1)
    n_proc_entry.pack()
    
    def submit():
        b = int(n_blk_entry.get())
        p = int(n_proc_entry.get())

        input_win.destroy()
        getinputMemA(b,p)
    
    frame_2_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_2_1.grid(row=2, column=1)
    submit_btn = tk.Button(master=frame_2_1, text="Submit", command=submit)
    submit_btn.pack()

    input_win.mainloop()
    
def getinputMemA(b,p):
    window = tk.Tk()
    window.title("Memory Allocation Input's")
    blockSize = []
    processSize = []
    
    frame = tk.Frame(window, borderwidth=1)
    frame.grid(row=0, column=0)
    lbl = tk.Label(master=frame, text="Block Sizes")
    lbl.pack()

    for i in range(b):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=0, column=i+1)
        entry = tk.Entry(frame)
        blockSize.append(entry)
        entry.pack()
        
    frame = tk.Frame(window, borderwidth=1)
    frame.grid(row=1, column=0)
    lbl = tk.Label(master=frame, text="Process Sizes")
    lbl.pack()

    for i in range(p):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=1, column=i+1)
        entry = tk.Entry(frame)
        processSize.append(entry)
        entry.pack()
             
    def first():
        matrix = []
        for obj in blockSize:
            temp = obj.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            matrix.append(temp)

        start = []
        for item in processSize:
            temp = item.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            start.append(temp)

        window.destroy()

        firstFit(matrix,b, start,p)
        
    def best():
        matrix = []
        for obj in blockSize:
            temp = obj.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            matrix.append(temp)

        start = []
        for item in processSize:
            temp = item.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            start.append(temp)

        window.destroy()

        bestFit(matrix,b, start,p)
        
    def worst():
        matrix = []
        for obj in blockSize:
            temp = obj.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            matrix.append(temp)

        start = []
        for item in processSize:
            temp = item.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            start.append(temp)

        window.destroy()

        worstFit(matrix,b, start,p)
        
    firstspace = tk.Frame(master=window, borderwidth=1)
    firstspace.grid(row=3, column=0)

    bestspace = tk.Frame(master=window, borderwidth=1 )
    bestspace.grid(row=3, column=1)
    
    worstspace = tk.Frame(master=window, borderwidth=1)
    worstspace.grid(row = 3, column = 2)

    first_btn = tk.Button(master=firstspace, text="First Fit", command = first)
    first_btn.pack()

    best_btn = tk.Button(master=bestspace, text="Best Fit", command= best)
    best_btn.pack()
    
    worst_btn = tk.Button(master=worstspace, text="Worst Fit", command= worst)
    worst_btn.pack()    
    window.mainloop()

def firstFit(blockSize, m, processSize, n):
    allocation = [-1] * n  
    for i in range(n): 
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                allocation[i] = j   
                blockSize[j] -= processSize[i]  
                break
                
    mem_win = tk.Tk()
    mem_win.title("output")
    mem_win.minsize(400, 300)
    frame = tk.Frame(master=mem_win)
    
    lbl = tk.Label(frame, text="FIRST FIT OUTPUT")
    lbl.pack()
    
    lbl_tit = tk.Label(frame,text= " Process No.   Process Size",background = 'blue')
    lbl_tit.pack()
    for i in range(n):
        frame.grid(row=i+1, column=0)
        text1 = " "+str(i + 1)+"\t"+str(processSize[i])
        lbl_h = tk.Label(frame,text=text1)
        lbl_h.pack()
        
        if allocation[i] != -1:  
            text2 = "Block Allocated : "+ str(allocation[i] + 1)
            lbl1 = tk.Label(frame,text = text2,background = 'green')
            lbl1.pack()
        else: 
            lbl2 = tk.Label(frame,text ="Block Not Allocated", background = 'red')
            lbl2.pack()
            
    frame.pack()
            
            
def bestFit(blockSize, m, processSize, n): 
    allocation = [-1] * n  
    for i in range(n):   
        bestIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if bestIdx == -1:  
                    bestIdx = j  
                elif blockSize[bestIdx] > blockSize[j]:  
                    bestIdx = j 
  
        if bestIdx != -1:  
            allocation[i] = bestIdx    
            blockSize[bestIdx] -= processSize[i]
            
    mem_win = tk.Tk()
    mem_win.title("output")
    mem_win.minsize(400, 300)
    frame = tk.Frame(master=mem_win)
    
    lbl = tk.Label(frame, text="BEST FIT OUTPUT")
    lbl.pack()
    
    lbl_tit = tk.Label(frame,text= " Process No.   Process Size",background = 'blue')
    lbl_tit.pack()
    for i in range(n):
        frame.grid(row=i+1, column=0)
        text1 = " "+str(i + 1)+"\t"+str(processSize[i])
        lbl_h = tk.Label(frame,text=text1)
        lbl_h.pack()
        
        if allocation[i] != -1:  
            text2 = "Block Allocated : "+ str(allocation[i] + 1)
            lbl1 = tk.Label(frame,text = text2,background = 'green')
            lbl1.pack()
        else: 
            lbl2 = tk.Label(frame,text ="Block Not Allocated", background = 'red')
            lbl2.pack()
            
    frame.pack()
            
            
def worstFit(blockSize, m, processSize, n): 
    allocation = [-1] * n 
    for i in range(n): 
        wstIdx = -1
        for j in range(m): 
            if blockSize[j] >= processSize[i]: 
                if wstIdx == -1:  
                    wstIdx = j  
                elif blockSize[wstIdx] < blockSize[j]:  
                    wstIdx = j  
        if wstIdx != -1:   
            allocation[i] = wstIdx  
            blockSize[wstIdx] -= processSize[i] 
  
    mem_win = tk.Tk()
    mem_win.title("output")
    mem_win.minsize(400, 300)
    frame = tk.Frame(master=mem_win)
    
    lbl = tk.Label(frame, text="WORST FIT OUTPUT")
    lbl.pack()
    
    lbl_tit = tk.Label(frame,text= " Process No.   Process Size",background = 'blue')
    lbl_tit.pack()
    for i in range(n):
        frame.grid(row=i+1, column=0)
        text1 = " "+str(i + 1)+"\t"+str(processSize[i])
        lbl_h = tk.Label(frame,text=text1)
        lbl_h.pack()
        
        if allocation[i] != -1:  
            text2 = "Block Allocated : "+ str(allocation[i] + 1)
            lbl1 = tk.Label(frame,text = text2,background = 'green')
            lbl1.pack()
        else: 
            lbl2 = tk.Label(frame,text ="Block Not Allocated", background = 'red')
            lbl2.pack()
            
    frame.pack()

            
if __name__ == '__main__':
    main()
   