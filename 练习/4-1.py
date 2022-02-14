from pythonds.basic.queue import Queue

def potato(a,n):
    s = Queue()
    for name in a:
        s.enqueue(name)
    
    while s.size() >1:
        for i in range(n):
            s.enqueue(s.dequeue())
        s.dequeue()
    
    return s.dequeue()

print(potato(['a','b', 'c', 'd', 'e', 'f'],5))