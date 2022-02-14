from pythonds.basic.queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.speed = ppm # 打印速度
        self.currentTask = None #现有任务，默认是None
        self.timeRemaining = 0 #现有任务时间
    
    def tick(self):
        #当前秒发生的事情
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining -1
            if self.timeRemaining <= 0:
                self.currentTask = None
    
    def busy(self):
        #是否正在任务
        if self.currentTask !=None:
            return True
        else:
            return False
    def startNext(self, newtask):
        self.currentTask = newtask
        #计算新任务时长
        self.timeRemaining = newtask.getPages() * 60/self.speed

class Task:
    def __init__(self, time):
        self.timestamp = time#生成时间戳
        self.pages = random.randrange(1,21)#task页数
    
    def getStamp(self):
        #时间戳
        return self.timestamp
    
    def getPages(self):
        #打印页数
        return self.pages
    
    def waitTime(self, currenttime):
        #等待时间
        return currenttime -self.timestamp

def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False

def simulation(numSeconds, speed):
    #生成一个打印机
    labprinter = Printer(speed)
    #task队列
    printQueue = Queue()

    waitingtimes = []

    for currentSceond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSceond)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSceond))
            labprinter.startNext(nexttask)
        labprinter.tick()
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("avarage wait %6.2f secs %3d tasks remaining." %(averageWait, printQueue.size()))

for i in range(10):
    print(simulation(3600,5))
