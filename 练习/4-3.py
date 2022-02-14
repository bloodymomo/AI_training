from pythonds.basic.deque import Deque
#回文词判定
def huiwenci(n:str):
    s = Deque()

    for st in n:
        s.addRear(st)
    
    equal = True

    while s.size()>1 and equal:
        r = s.removeRear()
        f = s.removeFront()
        if r!= f:
            equal = False
            return equal
    
    return equal

print(huiwenci("abba"))
