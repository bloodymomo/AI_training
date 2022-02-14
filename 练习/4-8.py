from pythonds.basic.queue import Queue

def radixSort(s):
    qlist = [Queue() for i in range(10)]
    mainQueue = Queue()

    for token in s:
        mainQueue.enqueue(token)
    
    #最大数位，决定轮数
    maxNum = str(max(s))
    maxLen = len(maxNum)

    for i in range(maxLen):


        for k in range(len(s)):
            #数字位数
            token = mainQueue.dequeue()
            tokenLen = len(str(token))
            #如果 token的位数>当前轮数，则返回当前轮数，token归入当前轮数的queue里
            if tokenLen >= i+1:
                #得到queue
                pos = int(str(token)[-i-1])
            else:
                pos = 0
            qlist[pos].enqueue(token)
        #将10个queue合并
        for j in range(10):
            while not qlist[j].isEmpty():
                mainQueue.enqueue(qlist[j].dequeue())
    res = []

    while not mainQueue.isEmpty():
        res.append(mainQueue.dequeue())
    
    return res

print(radixSort([8, 91, 34, 22, 65, 30, 4, 55, 18]))