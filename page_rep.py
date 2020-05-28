import tkinter as tk
import numpy as np

def main():
    mainwindow = tk.Tk()
    mainwindow.title("OS Simulator")
    mainwindow.minsize(400, 300)
    matdisplay_btn = tk.Button(master=mainwindow, text="Page Replacement Algorithm", command=getinputPagerep,background="cyan")
    matdisplay_btn.pack()
    mainwindow.mainloop()
    
def getinputPagerep():
    input_win = tk.Tk()
    input_win.title("Page Replacement Algorithm Inputs")

    frame_0_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_0.grid(row=0, column=0)
    m_frame_lbl = tk.Label(master=frame_0_0, text="Number of frames",background="yellow")
    m_frame_lbl.pack()

    frame_1_0 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_0.grid(row=1, column=0)
    n_seq_lbl = tk.Label(master=frame_1_0, text="Size of the sequence",background="yellow")
    n_seq_lbl.pack()

    frame_0_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_0_1.grid(row=0, column=1)
    m_frame_entry = tk.Entry(master=frame_0_1)
    m_frame_entry.pack()

    frame_1_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_1_1.grid(row=1, column=1)
    n_seq_entry = tk.Entry(master=frame_1_1)
    n_seq_entry.pack()

    def submit():
        m = int(m_frame_entry.get())
        n = int(n_seq_entry.get())

        input_win.destroy()
        get_input_Pagerep(m,n)

    frame_2_1 = tk.Frame(master=input_win, borderwidth=1)
    frame_2_1.grid(row=2, column=1)
    submit_btn = tk.Button(master=frame_2_1, text="Submit", command=submit,background="green",foreground="white",highlightcolor="blue")
    submit_btn.pack()

    input_win.mainloop()

def __fifolruoptimal(seq,n,m):

    lst=[]
    pagef=[]

    print("1.FIFO")
    f = -1
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == seq[i]):
                flag = 1
                break

        if flag == 0:
            f=(f+1)%m
            page[f] = seq[i]
            page_faults+=1
            print("\n%d ->" % (seq[i])),
            for j in range(m):
                if page[j] != -1:
                    print (page[j]),
                else:
                    print ("-"),
        else:
            print ("\n%d -> No Page Fault" % (seq[i])),

    print ("\n Total page faults : %d.\n\n" % (page_faults))

    lst.append(page)
    pagef.append(page_faults)

    print("2.LRU")

    x = 0
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == seq[i]):
                flag = 1
                break

        if flag == 0:
            if page[x] != -1:
                min = 999
                for k in range(m):
                    flag = 0
                    j =  i
                    while j>=0:
                        j-=1
                        if(page[k] == seq[j]):
                            flag = 1
                            break
                    if (flag == 1 and min > j):
                        min = j
                        x = k

            page[x] = seq[i]
            x=(x+1)%m
            page_faults+=1
            print ("\n%d ->" % (seq[i])),
            for j in range(m):
                if page[j] != -1:
                    print (page[j]),
                else:
                    print ("-"),
        else:
            print ("\n%d -> No Page Fault" % (seq[i])),

    print ("\n Total page faults : %d.\n\n" % (page_faults))

    lst.append(page)
    pagef.append(page_faults)



    print("3.OPTIMAL")

    x = 0
    page_faults = 0
    page = []
    for i in range(m):
        page.append(-1)

    for i in range(n):
        flag = 0
        for j in range(m):
            if(page[j] == seq[i]):
                flag = 1
                break

        if flag == 0:
            if page[x] != -1:
                max = -1
                for k in range(m):
                    flag = 0
                    j =  i
                    while j<n-1:
                        j+=1
                        if(page[k] == seq[j]):
                            flag = 1
                            break
                    if (flag == 1 and max < j):
                        max = j
                        x = k

            page[x] = seq[i]
            x=(x+1)%m
            page_faults+=1
            print ("\n%d ->" % (seq[i])),
            for j in range(m):
                if page[j] != -1:
                    print (page[j]),
                else:
                    print ("-"),
        else:
            print ("\n%d -> No Page Fault" % (seq[i])),

    print ("\n Total page faults : %d." % (page_faults))


    lst.append(page)
    pagef.append(page_faults)

    text="\nFinal frame contents:\n1.FIFO "+str(lst[0])+"\n2.LRU "+str(lst[1])+"\n3.OPTIMAL "+str(lst[2])+"\nTotal page faults:\n\
    1.FIFO :"+str(pagef[0])+"\n2.LRU :"+str(pagef[1])+"\n3.OPTIMAL :"+str(pagef[2])+"\n"

    __fifolruoptimal_win = tk.Tk()
    __fifolruoptimal_win.title("Page Replacement Algorithm Output")
    __fifolruoptimal_win.minsize(400, 300)
    frame = tk.Frame(master=__fifolruoptimal_win)
    seq_lbl = tk.Label(master=frame, text=text)

    seq_lbl.pack()
    frame.pack()

    __fifolruoptimal_win.mainloop()


def get_input_Pagerep(m,n):
    window = tk.Tk()
    window.title("Page Replacment Algorithm Input")
    a=[]


    frame = tk.Frame(window, borderwidth=1)
    frame.grid(row=0, column=0)

    lbl = tk.Label(master=frame, text="Sequence:\n(Input only positive values)",background="yellow")

    lbl.pack()

    for i in range(n):
        frame = tk.Frame(window, borderwidth=1)
        frame.grid(row=i+1, column=2)
        entry = tk.Entry(master=frame)
        a.append(entry)
        entry.pack()



    def takesum():
        seq = []
        for obj in a:
            temp = obj.get()
            try:
                temp = int(temp)
            except ValueError:
                temp = 0
            seq.append(temp)



        seq = np.array(seq).reshape(n)

        window.destroy()

        __fifolruoptimal(seq,n,m)


    submitspace = tk.Frame(master=window, borderwidth=1)
    submitspace.grid(row=m+3, column=2*n)

    quitspace = tk.Frame(master=window, borderwidth=1 )
    quitspace.grid(row=m+3, column=3)

    quit_btn = tk.Button(master=quitspace, text="Quit", command = window.destroy,background="red",foreground="white")
    quit_btn.pack()

    submit_btn = tk.Button(master=submitspace, text="Submit", command=takesum,background="green",foreground="white")
    submit_btn.pack()

    window.mainloop()
 
    
