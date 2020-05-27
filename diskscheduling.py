import tkinter as tk


def diskScheduling(req, startHead, noOfIndex, dir, min, max, outputFrame):

    ####################
    #  FCFS

    totalSeek, distance, curHead = 0, 0, 0
    seekSeq = []
    head = startHead

    for i in range(noOfIndex):
        curHead = req[i]

        seekSeq.append(curHead)

        distance = abs(curHead - head)

        totalSeek += distance

        head = curHead

    print('FCFS')
    print('Total number of seeks: {}'.format(totalSeek))
    print(seekSeq)

    T1 = tk.Text(outputFrame, height=4, width=30)
    T1.pack()
    T1.insert(tk.INSERT, "FCFS\n")
    T1.insert(tk.INSERT, 'Total number of seeks: {}\n'.format(totalSeek))
    T1.insert(tk.INSERT, 'Seek Sequence\n')
    T1.insert(tk.END, seekSeq)

    ####################
    #  SSTF

    totalSeek, distance, curHead, leastDis, leastInd = 0, 0, 0, 999, -1
    done = [False for i in range(noOfIndex)]
    seekSeq = []
    head = startHead

    for i in range(noOfIndex):
        leastDis = 999

        # Loop for finding shortest distacnee from current head
        for j in range(noOfIndex):
            if done[j] == True:
                continue
            else:
                curHead = req[j]

                distance = abs(curHead - head)

                if distance < leastDis:
                    leastDis = distance
                    leastInd = j

        curHead = req[leastInd]

        done[leastInd] = True

        seekSeq.append(curHead)

        totalSeek += leastDis

        head = curHead

    print('SSTF')
    print('Total number of seeks: {}'.format(totalSeek))
    print(seekSeq)

    T2 = tk.Text(outputFrame, height=4, width=30)
    T2.pack()
    T2.insert(tk.INSERT, "SSTF\n")
    T2.insert(tk.INSERT, 'Total number of seeks: {}\n'.format(totalSeek))
    T2.insert(tk.INSERT, 'Seek Sequence\n')
    T2.insert(tk.END, seekSeq)

    ####################
    #  SCAN

    totalSeek, distance, curHead = 0, 0, 0
    seekSeq, left, right = [], [], []
    head = startHead

    for i in range(noOfIndex):
        if req[i] < head:
            left.append(req[i])
        else:
            right.append(req[i])

    if dir == 0:
        left.sort(reverse=True)
        right.sort()

        for k in left:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

        # Setting index to min (set to 0)

        curHead = min

        seekSeq.append(min)

        distance = abs(curHead - head)

        totalSeek += distance

        head = curHead

        for k in right:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead
    else:
        left.sort(reverse=True)
        right.sort()

        for k in right:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

        # Setting index to max

        curHead = max

        seekSeq.append(max)

        distance = abs(curHead - head)

        totalSeek += distance

        head = curHead

        for k in left:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

    print('SCAN')
    print('Total number of seeks: {}'.format(totalSeek))
    print(seekSeq)

    T3 = tk.Text(outputFrame, height=4, width=30)
    T3.pack()
    T3.insert(tk.INSERT, "SCAN\n")
    T3.insert(tk.INSERT, 'Total number of seeks: {}\n'.format(totalSeek))
    T3.insert(tk.INSERT, 'Seek Sequence\n')
    T3.insert(tk.END, seekSeq)

    ####################
    #  CSCAN

    totalSeek, distance, curHead = 0, 0, 0
    seekSeq, left, right = [], [], []
    head = startHead

    for i in range(noOfIndex):
        if req[i] < head:
            left.append(req[i])
        else:
            right.append(req[i])

    if dir == 0:
        left.sort(reverse=True)
        right.sort(reverse=True)

        for k in left:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

        # Setting index to min

        curHead = min

        seekSeq.append(min)

        distance = abs(curHead - head)

        totalSeek += distance

        head = curHead

        # Setting index to max (Distance is not calcualted)

        head = max

        seekSeq.append(max)

        for k in right:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead
    else:
        left.sort()
        right.sort()

        for k in right:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

        # Setting index to max

        curHead = max

        seekSeq.append(max)

        distance = abs(curHead - head)

        totalSeek += distance

        head = curHead

        # Setting index to min (Distance is not calcualted)

        head = min

        seekSeq.append(min)

        for k in left:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

    print('CSCAN')
    print('Total number of seeks: {}'.format(totalSeek))
    print(seekSeq)

    T4 = tk.Text(outputFrame, height=4, width=30)
    T4.pack()
    T4.insert(tk.INSERT, "CSCAN\n")
    T4.insert(tk.INSERT, 'Total number of seeks: {}\n'.format(totalSeek))
    T4.insert(tk.INSERT, 'Seek Sequence\n')
    T4.insert(tk.END, seekSeq)

    ####################
    #  LOOK

    totalSeek, distance, curHead = 0, 0, 0
    seekSeq, left, right = [], [], []
    head = startHead

    for i in range(noOfIndex):
        if req[i] < head:
            left.append(req[i])
        else:
            right.append(req[i])

    if dir == 0:
        left.sort(reverse=True)
        right.sort()

        for k in left:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

        for k in right:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead
    else:
        left.sort(reverse=True)
        right.sort()

        for k in right:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

        for k in left:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

    print('LOOK')
    print('Total number of seeks: {}'.format(totalSeek))
    print(seekSeq)

    T5 = tk.Text(outputFrame, height=4, width=30)
    T5.pack()
    T5.insert(tk.INSERT, "LOOK\n")
    T5.insert(tk.INSERT, 'Total number of seeks: {}\n'.format(totalSeek))
    T5.insert(tk.INSERT, 'Seek Sequence\n')
    T5.insert(tk.END, seekSeq)

    ####################
    #  CLOOK

    totalSeek, distance, curHead = 0, 0, 0
    seekSeq, left, right = [], [], []
    head = startHead

    for i in range(noOfIndex):
        if req[i] < head:
            left.append(req[i])
        else:
            right.append(req[i])

    if dir == 0:
        left.sort(reverse=True)
        right.sort(reverse=True)

        for k in left:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

        for k in right:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead
    else:
        left.sort()
        right.sort()

        for k in right:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

        for k in left:
            curHead = k

            seekSeq.append(k)

            distance = abs(curHead - head)

            totalSeek += distance

            head = curHead

    print('CLOOK')
    print('Total number of seeks: {}'.format(totalSeek))
    print(seekSeq)

    T6 = tk.Text(outputFrame, height=4, width=30)
    T6.pack()
    T6.insert(tk.INSERT, "LOOK\n")
    T6.insert(tk.INSERT, 'Total number of seeks: {}\n'.format(totalSeek))
    T6.insert(tk.INSERT, 'Seek Sequence\n')
    T6.insert(tk.END, seekSeq)


def checkInputs(entries):

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


def onSubmitClickFirst():

    if checkInputs([maxEntry, dirEntry, headEntry, noOfIndexEntry]):
        errorText.set('')

        if int(dirEntry.get()) == 0 or int(dirEntry.get()) == 1:
            errorText.set('')
        else:
            errorText.set('Enter correct direction')
            return False
    else:
        return False

    for i in range(int(noOfIndexEntry.get())):
        tk.Label(middleFrame, text="Enter index {}: ".format(i+1)).grid(row=i+5)
        newEntry = tk.Entry(middleFrame)
        newEntry.grid(row=i+5, column=1)
        indexEntries.append(newEntry)

    submitBtn = tk.Button(bottomFrame, text='Submit',
                          command=onSubmitClickSecond)
    submitBtn.grid(row=0, column=1, padx=10, pady=10)


def onSubmitClickSecond():

    if checkInputs(indexEntries):
        errorText.set('')
    else:
        return False

    maxInput = int(maxEntry.get())
    dirInput = int(dirEntry.get())
    headInput = int(headEntry.get())
    noOfIndexInput = int(noOfIndexEntry.get())

    indices = []

    for i in range(noOfIndexInput):
        indices.append(int(indexEntries[i].get()))

    output = tk.Tk()
    output.title('Disk Scheduling - Output')

    outputFrame = tk.Frame(output)
    outputFrame.pack()

    tk.Label(output, text='Disk Scheduling').pack()

    diskScheduling(indices, headInput, noOfIndexInput, dirInput, 0, maxInput, outputFrame)

    submitBtn = tk.Button(bottomFrame, text='Submit', state=tk.DISABLED)
    submitBtn.grid(row=0, column=1, padx=10, pady=10)


if __name__ == '__main__':

    curStep = 1
    indexEntries = []

    window = tk.Tk()
    window.title('Disk Scheduling - Input')

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

    tk.Label(middleFrame, text='Enter max input: ').grid(row=1)
    maxEntry = tk.Entry(middleFrame, width=20)
    maxEntry.grid(row=1, column=1)

    tk.Label(middleFrame, text='Enter direction (left/right) => (0/1): ').grid(row=2)
    dirEntry = tk.Entry(middleFrame)
    dirEntry.grid(row=2, column=1)

    tk.Label(middleFrame, text='Enter head initial location: ').grid(row=3)
    headEntry = tk.Entry(middleFrame)
    headEntry.grid(row=3, column=1)

    tk.Label(middleFrame, text='Enter no of indices: ').grid(row=4)
    noOfIndexEntry = tk.Entry(middleFrame)
    noOfIndexEntry.grid(row=4, column=1)

    quitBtn = tk.Button(bottomFrame, text='Quit', command=lambda: exit())
    quitBtn.grid(row=0, column=0, padx=10, pady=10)

    submitBtn = tk.Button(bottomFrame, text='Submit',
                          command=onSubmitClickFirst)
    submitBtn.grid(row=0, column=1, padx=10, pady=10)

    window.mainloop()

    # max = int(input('Enter max input: '))

    # dir = int(input('Enter direction (left / right) => (0 / 1)'))

    # head = int(input('Enter head starting location: '))

    # noOfIndex = int(input('Enter number of index: '))

    # reqSeq = []

    # for i in range(noOfIndex):
    #     str = 'Enter index no {}: '.format(i + 1)
    #     ind = int(input(str))
    #     reqSeq.append(ind)

    # diskScheduling(reqSeq, head, noOfIndex, dir, 0, max)

# Test input
# 199
# 0
# 50
# 8
# 176
# 79
# 34
# 60
# 92
# 11
# 41
# 114

# Output
# FCFS
# Total number of seeks: 510
# [176, 79, 34, 60, 92, 11, 41, 114]
# SSTF
# Total number of seeks: 204
# [41, 34, 11, 60, 79, 92, 114, 176]
# SCAN
# Total number of seeks: 226
# [41, 34, 11, 0, 60, 79, 92, 114, 176]
# CSCAN
# Total number of seeks: 189
# [41, 34, 11, 0, 199, 176, 114, 92, 79, 60]
# LOOK
# Total number of seeks: 204
# [41, 34, 11, 60, 79, 92, 114, 176]
# CLOOK
# Total number of seeks: 320
# [41, 34, 11, 176, 114, 92, 79, 60]
