from operator import itemgetter
from tkinter import ttk
import tkinter as tk
import copy

def makeTable(process, outputFrame, text):

    tk.Label(outputFrame, text=text).pack()

    table = ttk.Treeview(outputFrame)
    table["columns"] = ("Process ID", "Arrival Time", "Burst Time",
                        "Turnaround Time", "Waiting Time", "Completed")
    table["show"] = "headings"
    table.heading("Process ID", text="Process ID")
    table.heading("Arrival Time", text="Arrival Time")
    table.heading("Burst Time", text="Burst Time")
    table.heading("Turnaround Time", text="Turnaround Time")
    table.heading("Waiting Time", text="Waiting Time")
    table.heading("Completed", text="Completed")

    index = 0

    for entry in process:
        table.insert("", index, index, values=(
            entry['pno'], entry['at'], entry['bt'], entry['tat'], entry['wt'], entry['complete']))
        index += 1

    table.pack()

def sjf(processes, n, outputFrame):
    process = sorted(processes, key=lambda i: i['at'])
    p = []
    t = process[0]['at']
    for j in range(n):
        p = []
        for i in range(n):
            if (process[i]['at'] <= t and process[i]['complete'] == False):
                p.append(process[i])
        if (len(p) == 0):
            t = process[j]['at']
            for i in range(n):
                if (process[i]['at'] <= t):
                    p.append(process[i])

        p = sorted(p, key=lambda i: i['bt'])
        t += p[0]['bt']
        tat = t - p[0]['at']
        wt = tat - p[0]['bt']
        for i in range(n):
            if (p[0]['pno'] == process[i]['pno']):
                process[i]['tat'] = tat
                process[i]['wt'] = wt
                process[i]['complete'] = True
                break

    process = sorted(process, key=lambda i: i['pno'])
    # for i in range(n):
    #     print(process[i])

    makeTable(process, outputFrame, 'Shortest Job First')


def srtf(process, n, outputFrame):
    process = sorted(process, key=lambda i: i['at'])
    t = process[0]['at']
    while len([p for p in process if p['complete'] == False]) > 0:
        p = []
        for i in range(n):
            if (process[i]['at'] <= t and process[i]['complete'] == False):
                p.append(process[i])
        if (len(p) == 0):
            for i in range(n):
                if (process[i]['at'] > t and process[i]['complete'] == False):
                    t = process[i]['at']
                    break
            for i in range(n):
                if (process[i]['at'] <= t and process[i]['complete'] == False):
                    p.append(process[i])
        p = sorted(p, key=lambda i: i['rt'])
        t += 1
        for i in range(n):
            if (p[0]['pno'] == process[i]['pno']):
                process[i]['rt'] -= 1
                if (process[i]['rt'] == 0):
                    process[i]['tat'] = t - p[0]['at']
                    process[i]['wt'] = process[i]['tat'] - process[i]['bt']
                    process[i]['complete'] = True
                    break
    process = sorted(process, key=lambda i: i['pno'])
    # for i in range(n):
    #     print(process[i])

    makeTable(process, outputFrame, 'Shortest Remaining Time First')
    


def rpr(process, n, tq, outputFrame):
    process = sorted(process, key=lambda i: i['at'])
    j = 0
    t = process[0]['at']
    p = []
    while len([p for p in process if p['complete'] == False]) > 0:
        p = []
        for i in range(n):
            if (process[i]['complete'] == False and process[i]['at'] <= t):
                p.append(process[i])
        if (len(p) == 0):
            for i in range(n):
                if (process[i]['complete'] == False and process[i]['at'] > t):
                    t = process[i]['at']
                    break
            for i in range(n):
                if (process[i]['complete'] == False and process[i]['at'] <= t):
                    p.append(process[i])
        j = 0
        while (len(p) != 0):
            for i in range(n):
                if (p[j]['pno'] == process[i]['pno'] and process[i]['complete'] == False):
                    temp = {}
                    if (process[i]['rt'] <= tq):
                        t += process[i]['rt']
                        process[i]['rt'] = 0
                        process[i]['complete'] = True
                        process[i]['tat'] = t - process[i]['at']
                        process[i]['wt'] = process[i]['tat'] - process[i]['bt']
                        p.pop(j)
                        j -= 1
                    else:
                        t += tq
                        process[i]['rt'] -= tq
                        temp = process[i]
                        p.pop(j)
                        j -= 1
                    for k in range(n):
                        if (process[k] not in p and process[k]['complete'] == False and process[k]['at'] <= t and process[k] != temp):
                            p.append(process[k])
                    if(temp != {}):
                        p.append(temp)
                    j += 1
                    break

    process = sorted(process, key=lambda i: i['pno'])
    # for i in range(n):
    #     print(process[i])

    makeTable(process, outputFrame, 'Round Robin')


def priorityPreemptive(process, n, outputFrame):
    process = sorted(process, key=lambda i: i['at'])
    t = process[0]['at']

    while len([p for p in process if p['complete'] == False]) > 0:
        p = []
        for i in range(n):
            if (process[i]['complete'] == False and process[i]['at'] <= t):
                p.append(process[i])
        if (len(p) == 0):
            for i in range(n):
                if (process[i]['at'] > t and process[i]['complete'] == False):
                    t = process[i]['at']
                    break
            for i in range(n):
                if (process[i]['complete'] == False and process[i]['at'] <= t):
                    p.append(process[i])

        p = sorted(p, key=lambda i: i['priority'])
        t += 1
        for i in range(n):
            if (p[0]['pno'] == process[i]['pno']):
                process[i]['rt'] -= 1
                if (process[i]['rt'] == 0):
                    process[i]['tat'] = t - process[i]['at']
                    process[i]['wt'] = process[i]['tat'] - process[i]['bt']
                    process[i]['complete'] = True
                break
    process = sorted(process, key=lambda i: i['pno'])
    # for i in range(n):
    #     print(process[i])

    makeTable(process, outputFrame, 'Priority Preemptive')


def priorityNonPreemptive(process, n, outputFrame):
    process = sorted(process, key=lambda i: i['at'])
    t = process[0]['at']
    p = []
    for j in range(n):
        p = []
        for i in range(n):
            if (process[i]['at'] <= t and process[i]['complete']==False):
                p.append(process[i])
        if (len(p) == 0):
            for i in range(n):
                if (process[i]['at'] > t and process[i]['complete'] == False):
                    t = process[i]['at']
                    break
            for i in range(n):
                if (process[i]['complete'] == False and process[i]['at'] <= t):
                    p.append(process[i])
        p = sorted(p, key=lambda i: i['priority'])
        t += p[0]['bt']
        for i in range(n):
            if (p[0]['pno'] == process[i]['pno']):
                process[i]['tat'] = t - process[i]['at']
                process[i]['wt'] = process[i]['tat'] - process[i]['bt']
                process[i]['complete'] = True
                break
    process = sorted(process, key=lambda i: i['pno'])
    # for i in range(n):
    #     print(process[i])

    makeTable(process, outputFrame, 'Priority Non Preemptive')


def fcfs(process, n, outputFrame):
    process = sorted(process, key=lambda i: i['at'])
    t = process[0]['at']
    for i in range(n):

        t = max(t, process[i]['at'])

        t += process[i]['bt']
        process[i]['tat'] = t - process[i]['at']
        process[i]['wt'] = process[i]['tat'] - process[i]['bt']
    process = sorted(process, key=lambda i: i['pno'])
    # for i in range(n):
    #     print(process[i])

    makeTable(process, outputFrame, 'First Come First Serve')


def schedulingAll(allProcesses, noOfProcessesInput, timeQuantumInput, outputFrame, output):
    n = noOfProcessesInput
    tq = timeQuantumInput

    processes = copy.deepcopy(allProcesses)
    sjf(processes, n, outputFrame)

    processes = copy.deepcopy(allProcesses)
    srtf(processes, n, outputFrame)

    processes = copy.deepcopy(allProcesses)
    rpr(processes, n, tq, outputFrame)

    processes = copy.deepcopy(allProcesses)
    priorityPreemptive(processes, n, outputFrame)

    processes = copy.deepcopy(allProcesses)
    fcfs(processes, n, outputFrame)

    processes = copy.deepcopy(allProcesses)
    priorityNonPreemptive(processes, n, outputFrame)


def checkInputs(entries, errorText):

    for entry in entries:
        if entry.get().strip() == '':
            errorText.set(
                'Please enter all inputs and make sure they are valid')
            return False
        elif not entry.get().isdecimal():
            errorText.set(
                'Please enter all inputs and make sure they are valid')
            return False

    return True


def checkInputsList(entries, errorText):

    for entryList in entries:
        for entry in entryList:
            if entry.get().strip() == '':
                errorText.set(
                    'Please enter all inputs and make sure they are valid')
                return False
            elif not entry.get().isdecimal():
                errorText.set(
                    'Please enter all inputs and make sure they are valid')
                return False

    return True


def onSubmitClickFirst(errorText, allProcessesEntry,  noOfProcessesEntry, timeQuantumEntry, bottomFrame, middleFrame, window):

    if checkInputs([noOfProcessesEntry, timeQuantumEntry], errorText):
        errorText.set('')
    else:
        return False

    for i in range(int(noOfProcessesEntry.get())):
        tk.Label(middleFrame, text="Enter arrival time of process {}: ".format(
            i+1)).grid(row=i+5+(i*3))
        processArrival = tk.Entry(middleFrame)
        processArrival.grid(row=i+5+(i*3), column=1)

        tk.Label(middleFrame, text="Burst time of process {}: ".format(
            i+1)).grid(row=i+6+(i*3))
        processBurst = tk.Entry(middleFrame)
        processBurst.grid(row=i+6+(i*3), column=1)

        tk.Label(middleFrame, text="Priority of the process {}: ".format(
            i+1)).grid(row=i+7+(i*3))
        processPriority = tk.Entry(middleFrame)
        processPriority.grid(row=i+7+(i*3), column=1)

        allProcessesEntry.append(
            [processArrival, processBurst, processPriority])

    submitBtn = tk.Button(bottomFrame, text='Submit',
                          command=lambda: onSubmitClickSecond(errorText, allProcessesEntry,  noOfProcessesEntry, timeQuantumEntry, bottomFrame, window))
    submitBtn.grid(row=0, column=1, padx=10, pady=10)


def onSubmitClickSecond(errorText, allProcessesEntry,  noOfProcessesEntry, timeQuantumEntry, bottomFrame, window):

    if checkInputsList(allProcessesEntry, errorText):
        errorText.set('')
    else:
        return False

    noOfProcessesInput = int(noOfProcessesEntry.get())
    timeQuantumInput = int(timeQuantumEntry.get())

    allProcesses = []

    for i in range(noOfProcessesInput):
        pno = i+1
        newProcess = {'pno': pno, 'at': int(allProcessesEntry[i][0].get()), 'bt': int(allProcessesEntry[i][1].get()), 'rt': int(allProcessesEntry[i][1].get()),
                      'tat': 0, 'wt': 0, 'complete': False, 'priority': int(allProcessesEntry[i][2].get())}
        allProcesses.append(newProcess)

    output = tk.Tk()
    output.title('Scheduling - Output')

    outputFrame = tk.Frame(output)
    outputFrame.pack()

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))

    canvas = tk.Canvas(outputFrame, width=1200, height=700)
    canvas.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(outputFrame, command=canvas.yview)
    scrollbar.pack(side=tk.LEFT, fill='y')

    canvas.configure(yscrollcommand = scrollbar.set)

    canvas.bind('<Configure>', on_configure)

    frame = tk.Frame(canvas)
    canvas.create_window((0,0), window=frame, anchor='nw')

    schedulingAll(allProcesses, noOfProcessesInput,
                  timeQuantumInput, frame, output)

    # submitBtn = tk.Button(bottomFrame, text='Submit', state=tk.DISABLED)
    # submitBtn.grid(row=0, column=1, padx=10, pady=10)

    window.destroy()


def scheduling():

    allProcessesEntry = []

    window = tk.Tk()
    window.title('Scheduling - Input')

    topFrame = tk.Frame(window)
    topFrame.pack()

    errorFrame = tk.Frame(window)
    errorFrame.pack()

    errorText = tk.StringVar()
    errorLabel = tk.Label(errorFrame, textvariable=errorText)
    errorLabel.pack()

    middleFrame = tk.Frame(window)
    middleFrame.pack()

    bottomFrame = tk.Frame(window)
    bottomFrame.pack()

    tk.Label(topFrame, text='Disk Scheduling').pack()

    tk.Label(middleFrame, text='Enter the number of processes : ').grid(row=1)
    noOfProcessesEntry = tk.Entry(middleFrame, width=20)
    noOfProcessesEntry.grid(row=1, column=1)

    tk.Label(middleFrame, text='Enter the time quantum (For RRP): ').grid(row=2)
    timeQuantumEntry = tk.Entry(middleFrame)
    timeQuantumEntry.grid(row=2, column=1)

    tk.Label(middleFrame, text="Note: Higher priority has lower number.").grid(row=0)
    

    quitBtn = tk.Button(bottomFrame, text='Quit', command=lambda: exit())
    quitBtn.grid(row=0, column=0, padx=10, pady=10)

    submitBtn = tk.Button(bottomFrame, text='Submit',
                          command=lambda: onSubmitClickFirst(errorText, allProcessesEntry, noOfProcessesEntry, timeQuantumEntry, bottomFrame, middleFrame, window))
    submitBtn.grid(row=0, column=1, padx=10, pady=10)

    window.mainloop()


# scheduling()
