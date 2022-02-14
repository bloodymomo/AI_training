class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self,newdata):
        self.data = newdata
    
    def setNext(self,newnext):
        self.next = newnext

def add(self, item):
    
    current = self.head
    previous = None
    stop = False
    #找到插入位置
    while current != None and not stop:
        if current.getData()> item:
            stop = True
        else:
            previous= current
            current = current.getNext()


    temp = Node(item)
    #如果插入最小的，插入表头
    if previous == None:
        temp.setNext(self.head)
        self.head = temp
    #如果插入中间
    else:
        temp.setNext(current)
        previous.setNext(temp)

def size(self):
    current = self.head
    count = 0
    while current != None:
        count = count +1
        current = current.getNext()
    return count


def search(self, item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
        if current.getData() == item:
            found = True
        else:
            #如果当前项> item，就可以停止item了

            if current.getData() > item:
                stop = True
            else:
                current = current.getNext()
    return found