import tkinter as tk
    
def getinputMA():
    input_win = tk.Tk()
    input_win.title("Memory Allocation methods")
    
    frame_0_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_0.grid(row=0, column=0)
    n_blk_lbl = tk.Label(master=frame_0_0, text="Number of Blocks")
    n_blk_lbl.pack()
    
    frame_1_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_0.grid(row=1, column=0)
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
    intf = 0
    exf = 0
    temp = []
    for i in range(m):
        temp.append(blockSize[i])
    
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
    
    lbl = tk.Label(frame, text="FIRST FIT OUTPUT").grid(row = 0,column = 2)
    
    lbl_tit = tk.Label(frame,text= " Process No",background = 'yellow',relief="ridge",borderwidth = 3,width = 10).grid(row = 1,column = 1)
    lbl_tit = tk.Label(frame,text= " Process Size",background = 'yellow',relief="ridge",borderwidth = 3,width = 10).grid(row = 1,column = 2)
    lbl_tit = tk.Label(frame,text= " Block No.",background = 'yellow',relief="ridge",borderwidth = 3,width = 20).grid(row = 1,column = 3)
    
    for i in range(n):
        text1 = str(i + 1)
        lbl_h = tk.Label(frame,text=text1,relief="ridge",borderwidth = 3,width = 10).grid(row = i+2,column = 1)
        text1 = str(processSize[i])
        lbl_h = tk.Label(frame,text=text1,relief="ridge",borderwidth = 3,width = 10).grid(row = i+2,column = 2)
        
        if allocation[i] != -1:  
            text2 = "Block Allocated : "+ str(allocation[i] + 1)
            lbl1 = tk.Label(frame,text = text2,background = '#90ee90',relief="ridge",borderwidth = 3,width = 20).grid(row = i+2,column = 3)
        else: 
            lbl2 = tk.Label(frame,text ="Block Not Allocated", background = '#ffcccb',relief="ridge",borderwidth = 3,width = 20).grid(row = i+2,column = 3)
            
    for i in range(m):
        if temp[i]==blockSize[i]:
            exf= exf + temp[i]
        else:
            intf= intf + blockSize[i]
            
    lbl = tk.Label(frame, text="Internal Fragmentation : "+ str(intf)).grid(row =n+3 ,column = 2)
    lbl = tk.Label(frame, text="External Fragmentation : "+str(exf)).grid(row = n+4,column = 2)

    frame.grid()
    
    
            
            
def bestFit(blockSize, m, processSize, n): 
    intf = 0
    exf = 0
    temp = []
    for i in range(m):
        temp.append(blockSize[i])
        
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
    
    lbl = tk.Label(frame, text="BEST FIT OUTPUT").grid(row = 0,column = 2)
    
    lbl_tit = tk.Label(frame,text= " Process No",background = 'yellow',relief="ridge",borderwidth = 3,width = 10).grid(row = 1,column = 1)
    lbl_tit = tk.Label(frame,text= " Process Size",background = 'yellow',relief="ridge",borderwidth = 3,width = 10).grid(row = 1,column = 2)
    lbl_tit = tk.Label(frame,text= " Block No.",background = 'yellow',relief="ridge",borderwidth = 3,width = 20).grid(row = 1,column = 3)
    
    for i in range(n):
        text1 = str(i + 1)
        lbl_h = tk.Label(frame,text=text1,relief="ridge",borderwidth = 3,width = 10).grid(row = i+2,column = 1)
        text1 = str(processSize[i])
        lbl_h = tk.Label(frame,text=text1,relief="ridge",borderwidth = 3,width = 10).grid(row = i+2,column = 2)
        
        if allocation[i] != -1:  
            text2 = "Block Allocated : "+ str(allocation[i] + 1)
            lbl1 = tk.Label(frame,text = text2,background = '#90ee90',relief="ridge",borderwidth = 3,width = 20).grid(row = i+2,column = 3)
        else: 
            lbl2 = tk.Label(frame,text ="Block Not Allocated", background = '#ffcccb',relief="ridge",borderwidth = 3,width = 20).grid(row = i+2,column = 3)
            
    for i in range(m):
        if temp[i]==blockSize[i]:
            exf= exf + temp[i]
        else:
            intf= intf + blockSize[i]
            
    lbl = tk.Label(frame, text="Internal Fragmentation : "+ str(intf)).grid(row =n+3 ,column = 2)
    lbl = tk.Label(frame, text="External Fragmentation : "+str(exf)).grid(row = n+4,column = 2)

    frame.grid()
            
            
def worstFit(blockSize, m, processSize, n): 
    intf = 0
    exf = 0
    temp = []
    for i in range(m):
        temp.append(blockSize[i])
        
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
    
    lbl = tk.Label(frame, text="WORST FIT OUTPUT").grid(row = 0,column = 2)
    
    lbl_tit = tk.Label(frame,text= " Process No",background = 'yellow',relief="ridge",borderwidth = 3,width = 10).grid(row = 1,column = 1)
    lbl_tit = tk.Label(frame,text= " Process Size",background = 'yellow',relief="ridge",borderwidth = 3,width = 10).grid(row = 1,column = 2)
    lbl_tit = tk.Label(frame,text= " Block No.",background = 'yellow',relief="ridge",borderwidth = 3,width = 20).grid(row = 1,column = 3)
    
    for i in range(n):
        text1 = str(i + 1)
        lbl_h = tk.Label(frame,text=text1,relief="ridge",borderwidth = 3,width = 10).grid(row = i+2,column = 1)
        text1 = str(processSize[i])
        lbl_h = tk.Label(frame,text=text1,relief="ridge",borderwidth = 3,width = 10).grid(row = i+2,column = 2)
        
        if allocation[i] != -1:  
            text2 = "Block Allocated : "+ str(allocation[i] + 1)
            lbl1 = tk.Label(frame,text = text2,background = '#90ee90',relief="ridge",borderwidth = 3,width = 20).grid(row = i+2,column = 3)
        else: 
            lbl2 = tk.Label(frame,text ="Block Not Allocated", background = '#ffcccb',relief="ridge",borderwidth = 3,width = 20).grid(row = i+2,column = 3)
            
    for i in range(m):
        if temp[i]==blockSize[i]:
            exf= exf + temp[i]
        else:
            intf= intf + blockSize[i]
            
    lbl = tk.Label(frame, text="Internal Fragmentation : "+ str(intf)).grid(row =n+3 ,column = 2)
    lbl = tk.Label(frame, text="External Fragmentation : "+str(exf)).grid(row = n+4,column = 2)

    frame.grid()

   