from pythonds.basic.queue import Queue

def func(S):
    # your code here
    q = Queue()
    minStr = S
    for i in S:
        q.enqueue(i)
    temp = 0
    while temp < q.size():
        first = q.dequeue()
        q.enqueue(first)
        newStr = ''.join(q.items)[::-1]
        if newStr < minStr:
            minStr = newStr
        temp = temp +1
    
    return minStr
    
#S = eval(input())
print(func("cba"))