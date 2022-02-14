from pythonds.basic.stack import Stack

def brack(a):

    s = Stack()
    res = True

    for i in a:
        print(i)
        if i in '([{':
            s.push(i)
        if i in ')]}':
            print('([{'.index(s.peek()))
            print(')]}'.index(i))
            if '([{'.index(s.peek()) == ')]}'.index(i):

                s.pop()
            else:
                res= False
                return res

    if not s.isEmpty():
        res = False

    return res

print(brack("{[(]})"))
