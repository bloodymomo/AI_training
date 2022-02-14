from pythonds.basic.queue import Queue

def func(mylist):
    q = Queue()
    res = []
    # for m in mylist:
    #     q.enqueue(m)

    i = 0
    while i < len(mylist):
        q.enqueue(mylist[i])
        print(q.items)
        while q.size() > 0 and mylist[i] - q.items[-1] > 10000:
            #先进的在队尾，从队尾dequeue
            print(q.items[0])
            q.dequeue()
        j = i + 1
        while j < len(mylist) and mylist[i] == mylist[j]:
            q.enqueue(j)
            j += 1
        res.append(q.size())
        while i < j:
            i += 1
    return res
mylist = eval(input())
print(func(mylist))
