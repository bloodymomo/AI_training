from pythonds.basic.queue import Queue
import random

def simulation(timePeriod, printSpeed):
    printQueue = Queue()

    busy = False
    currentTask =0
    waitTime =[]
    currentTaskRemain = 0
    taskPage = 0

    for t in range(timePeriod):
        if random.randrange(1,181) == 180:
            time = random.randrange(1,21)
            waitTime.append(time)
            printQueue.enqueue([t,time])
            if printQueue.isEmpty():
                currentTaskRemain= time
        if currentTaskRemain != 0:


        

