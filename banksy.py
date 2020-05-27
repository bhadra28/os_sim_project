import tkinter as tk
import numpy as np




soln = []
def safety(alloc, available, maxi, need, marked, seq, r):
    global soln

    if len(seq)==r:
        soln.append(seq)
        return

    for i in range(r):
        
        if marked[i]==False and (need[i, :] <= available).all():
            marked[i]=True
            
            available+=alloc[i, :]
            
            seq.append(i)
            safety(alloc, available, maxi, need, marked, seq, r)
            seq.pop()

            marked[i]=False

            available-=alloc[i, :]


def bankers(alloc, available, maxi, r, c):
    need = maxi - alloc
    

    marked = [False]*r
    seq = []
    check = True
    ans = True
    
    safety(alloc, available, maxi, need, marked, seq, r)
    global soln
    print(soln)
    



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


alloc = [[0, 1, 0 ],[ 2, 0, 0 ], 
            [3, 0, 2 ],[2, 1, 1] ,[ 0, 0, 2]] 

alloc = np.array(alloc).reshape(5, 3)

    # MAX Matrix  
maxi = [[7, 5, 3 ],[3, 2, 2 ], 
        [ 9, 0, 2 ],[2, 2, 2],[4, 3, 3]] 
maxi = np.array(maxi).reshape(5,3)
avail = [3, 3, 2] # Available Resources

bankers(alloc, avail, maxi, 5, 3)
