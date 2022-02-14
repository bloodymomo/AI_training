#开心消消乐
from pythonds.basic.stack import Stack


def xiaoxiao(a):
    s = Stack()
    res = ""
    for i in a:
        if s.isEmpty():
            s.push(i)
        elif s.peek() == i:
            s.pop()
            continue
        else:
            s.push(i)

    if s.isEmpty():
        return "None"
    else:
        while not s.isEmpty():
            res = res + s.pop()
    return res


print(xiaoxiao("kxkx"))
