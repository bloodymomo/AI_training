from pythonds.basic.stack import Stack


def infixToPostfix(infix):
    prec = {}  # 优先级字典
    prec['*'] = 3
    prec['/'] = 3
    prec['+'] = 2
    prec['-'] = 2
    prec['('] = 1

    infixList = infix.split()
    s = Stack()
    res = []

    for i in infixList:

        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or i in "0123456789" or i in "abcdefghijklmnopqrstuvwxyz":
            res.append(i)
            #Abc。。进入list
        elif i == '(':
            s.push(i)
            #遇到 ），stack.pop()出栈，知道第一个 （  出栈
        elif i == ')':
            temp = s.pop()
            while temp != '(':
                res.append(temp)
                temp = s.pop()
            #遇到 ），stack.pop()出栈，知道第一个 （  出栈
        else:
            while (not s.isEmpty()) and ((prec[s.peek()] >= prec[i])):
                #如果 栈顶 peek() 优先度 > =遇到的符号，
                #则先出栈，直到栈内没有更高（或同等）优先度的，遇到的符号进栈
                res.append(s.pop())
            s.push(i)
    while not s.isEmpty():
        res.append(s.pop())

    r = "".join(res)
    #整个输入读取完后，清空栈，全加入res里

    return r


print(infixToPostfix("( 4 + 2 ) * ( 3 - 5 )"))
