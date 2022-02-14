from pythonds.basic.stack import Stack


def calcuPostflex(postflex):
    s = Stack()
    postList = postflex.split(" ")
    for i in postList:

        if i not in "+-*/":  # 数字进栈
            s.push(i)
            print(i)

        if i in "+-*/":
            a = s.pop()
            b = s.pop()
            temp = str(b) + i + str(a)  # b先进栈，所以b在前
            result = eval(temp)
            print(result)
            s.push(result)

    return s.pop()


print(calcuPostflex("7 8 + 3 2 + /"))
