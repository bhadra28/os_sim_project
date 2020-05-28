import threading
import random
import time

import concurrent.futures
import logging
import queue

from random import randint
from time import sleep

import tkinter as tk
import os

import queue

from multiprocessing import Process, Queue, cpu_count
 
# from tkinter import *

class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(tw, text=self.text, justify=tk.LEFT,
                      background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    def enter(event):
        toolTip.showtip(text)
    def leave(event):
        toolTip.hidetip()
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


# Dining philosophers, 5 Phillies with 5 forks. Must have two forks to eat.
#
# Deadlock is avoided by never waiting for a fork while holding a fork (locked)
# Procedure is to do block while waiting to get first fork, and a nonblocking
# acquire of second fork.  If failed to get second fork, release first fork,
# swap which fork is first and which is second and retry until getting both.
#  
 
class Philosopher(threading.Thread):
 
    running = True
 
    def __init__(self, xname, forkOnLeft, forkOnRight):
        threading.Thread.__init__(self)
        self.name = xname
        self.forkOnLeft = forkOnLeft
        self.forkOnRight = forkOnRight
 
    def run(self):
        while(self.running):
            #  Philosopher is thinking (but really is sleeping).
            time.sleep( random.uniform(1,2))
            print ('%s is hungry.' % self.name, file=open("oplogs/dp.txt", "a"))
            self.dine()
 
    def dine(self):
        fork1, fork2 = self.forkOnLeft, self.forkOnRight
 
        while self.running:
            fork1.acquire(True)
            locked = fork2.acquire(False)
            if locked: break
            fork1.release()
            print ('%s swaps forks' % self.name, file=open("oplogs/dp.txt", "a"))
            # self.TBox.insert(tk.INSERT, '{} swaps forks'.format(self.name))
            fork1, fork2 = fork2, fork1
        else:
            return
 
        self.dining()
        fork2.release()
        fork1.release()
 
    def dining(self):			
        print ('%s starts eating '% self.name, file=open("oplogs/dp.txt", "a"))
        
        time.sleep(random.uniform(0,1))
        print ('%s finishes eating and leaves to think.' % self.name, file=open("oplogs/dp.txt", "a"))
 
def dp():

    def on_configure(event):
        canvas.configure(scrollregion=canvas.bbox('all'))


    root = tk.Tk()
    root.title("Dining Philosophers")


    canvas = tk.Canvas(root, height=600, width=400)
    canvas.pack(side=tk.LEFT)

    yscroll = tk.Scrollbar(root, command=canvas.yview)
    yscroll.pack(side=tk.LEFT, fill='y')

    canvas.configure(yscrollcommand = yscroll.set)

    canvas.bind('<Configure>', on_configure)

    

    frame = tk.Frame(canvas, background='white')
    canvas.create_window((0,0), window=frame, anchor='nw')

    f = open("oplogs/dp.txt", 'w')
    f.close()

    forks = [threading.Lock() for n in range(5)]
    philosopherNames = ('Zeno','Seneca','Nietzsche','Aristotle', 'Buchanan')
 
    philosophers= [Philosopher(philosopherNames[i], forks[i%5], forks[(i+1)%5]) for i in range(5)]
 
    random.seed()
    Philosopher.running = True
    for p in philosophers: p.start()
    time.sleep(3)
    Philosopher.running = False
    print ("Now we're finishing.", file=open("oplogs/dp.txt", "a"))

    f = open("oplogs/dp.txt", 'r')

    for line in f.readlines():
        lbl = tk.Label(frame, text = line, background='white')
        lbl.pack()

    os.remove('oplogs/dp.txt')
    root.mainloop()

#Use this to call Dining-Philosoper function
# dp()


class ReaderWriter():
    def __init__(self):
        self.rd = threading.Semaphore()  #initializing semaphores using Semaphore class in 
                                         #threading module for reading and wrting
        self.wrt = threading.Semaphore()  

        self.readCount = 0   #initializing number of reader present

    def reader(self):
        while True:
            self.rd.acquire()      #wait on read semaphore 

            self.readCount+=1       #increase count for reader by 1

            if self.readCount == 1: #since reader is present, prevent writing on data
                self.wrt.acquire() #wait on write semaphore

            self.rd.release()     #sinal on read semaphore

            print ("Reader ",{self.readCount}," is reading")

            self.rd.acquire()   #wait on read semaphore 

            self.readCount-=1   #reading performed by reader hence decrementing readercount

            if self.readCount == 0: #if no reader is present allow writer to write the data
                self.wrt.release()  # signal on write semphore, now writer can write

            self.rd.release()      #sinal on read semaphore

            time.sleep(0.05)          

    def writer(self):
        while True:
            self.wrt.acquire()     #wait on write semaphore

            print("Wrting data.....")  # write the data
            print("-"*20)

            self.wrt.release()      #sinal on write semaphore

            time.sleep(0.05)    

    def main(self):
        # calling mutliple readers and writers
        t1 = threading.Thread(target = self.reader) 
        t1.start()
        t2 = threading.Thread(target = self.writer) 
        t2.start()
        t3 = threading.Thread(target = self.reader) 
        t3.start()
        t4 = threading.Thread(target = self.reader) 
        t4.start()
        t6 = threading.Thread(target = self.writer) 
        t6.start()
        t5 = threading.Thread(target = self.reader) 
        t5.start()
        

def rw():
    c=ReaderWriter()
    c.main()

#Use this to call Reader Writer
# rw()



def pc():
    def producer(queue, event):
        """Pretend we're getting a number from the network."""
        while not event.is_set():
            message = random.randint(1, 101)
            logging.info("Producer got message: %s", message)
            queue.put(message)

        logging.info("Producer received event. Exiting")

    def consumer(queue, event):
        """Pretend we're saving a number in the database."""
        while not event.is_set() or not queue.empty():
            message = queue.get()
            logging.info(
                "Consumer storing message: %s (size=%d)", message, queue.qsize()
            )

        logging.info("Consumer received event. Exiting")

    if __name__ == "__main__":
        format = "%(asctime)s: %(message)s"
        logging.basicConfig(format=format, level=logging.INFO,
                            datefmt="%H:%M:%S")

        pipeline = queue.Queue(maxsize=10)
        event = threading.Event()
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(producer, pipeline, event)
            executor.submit(consumer, pipeline, event)

            time.sleep(0.1)
            logging.info("Main: about to set event")
            event.set()
            
#Use this to call Producer Consumer        
# pc()


def sb():

    CUSTOMERS = 50
    BARBERS = 3

    WAITING_ROOM = 15

    ARRIVAL_WAIT = 0.01


    def wait():
        time.sleep(ARRIVAL_WAIT * random.random())

    class Barber(threading.Thread):
        condition = threading.Condition()
        customers = []
        should_stop = threading.Event()

        def run(self):
                while self.should_stop.isSet() == False:
                        with self.condition:
                                if not self.customers:
                                        # No customers, snore...
                                        print("No Customers...", file=open("oplogs/sb.txt", "a"))
                                        time.sleep(0.1 * random.random())
                                # Get the next customer
                                if self.customers:
                                        current_customer = self.customers[0]
                                        print("A new customer has sat down...   ", file=open("oplogs/sb.txt", "a"))
                        # Actually service the next customer
                        if self.customers:
                                self.customers.pop(0)
                                current_customer.trim()
                                while current_customer.serviced.isSet() ==  False:
                                        Customer().wait()

    class Customer(threading.Thread):
        WAIT = 0.05
        def wait(self):
                time.sleep(self.WAIT * random.random())

        def trim(self):  # Called from Barber thread
                # Get a haircut
                print("Cutting hair...   ", file=open("oplogs/sb.txt", "a"))
                time.sleep(0.1 * random.random())
                print("Haircut finished   ", file=open("oplogs/sb.txt", "a"))
                self.serviced.set()
                
        def run(self):
                self.serviced = threading.Event()
                # Grab the barbers' attention, add ourselves to the customers,
                # and wait to be serviced
                if len(Barber().customers) < WAITING_ROOM:
                        print("A new customer has entered...   ", file=open("oplogs/sb.txt", "a"))
                        Barber().customers.append(self)
                else:
                        print("Waiting room full, customer leaving...   ", file=open("oplogs/sb.txt", "a"))
                        self.serviced.set()
                while self.serviced.isSet() == False:
                        self.wait()

    if __name__ == '__main__':
        barbers = []

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox('all'))


        root = tk.Tk()
        root.title("Sleeping Barbers")


        canvas = tk.Canvas(root, height=600, width=400)
        canvas.pack(side=tk.LEFT)

        yscroll = tk.Scrollbar(root, command=canvas.yview)
        yscroll.pack(side=tk.LEFT, fill='y')

        canvas.configure(yscrollcommand = yscroll.set)

        canvas.bind('<Configure>', on_configure)

        

        frame = tk.Frame(canvas, background='white')
        canvas.create_window((0,0), window=frame, anchor='nw')

        f = open("oplogs/sb.txt", 'w')
        f.close()


        print("Shop Opened", file=open("oplogs/sb.txt", "a"))
        for i in range(BARBERS):
                b = Barber()
                barbers.append(b)
                b.start()
        all_customers = []
        for c in range(CUSTOMERS):
                wait()
                c = Customer()
                all_customers.append(c)
                c.start()
        for c in all_customers:
                c.join()  # Wait for all customers to leave
        Barber().should_stop.set()
        for b in barbers:
                b.join()  # Wait for the barbers to finish completely
        print("All done for the day, Barber(s) leaving", file=open("oplogs/sb.txt", "a"))

        f = open("oplogs/sb.txt", 'r')

        for line in f.readlines():
            lbl = tk.Label(frame, text = line, background='white')
            lbl.pack()

        os.remove('oplogs/sb.txt')
        root.mainloop()
        
#Use this to call Sleeping Barber
# sb()



