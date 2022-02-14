from pythonds.basic.stack import Stack


def balance(n):

    l = len(n)
    s = Stack()
    res = True
    for i in range(l):
        # if n[i] == '(':
        if n[i] in '([{':  # 通用版
            s.push(n[i])
        if n[i] in ')]}' and s.isEmpty() == True:
            res = False

        if n[i] in ')]}' and s.isEmpty() == False:
            a = s.pop()
            if match(a, n[i]):  # pop出的左侧要与遇到的右侧对应
                res = True
            else:
                res = False
    if s.isEmpty() == False:
        res = False
    return res


def match(a, b):  # pop出的左侧要与遇到的右侧对应
    return "([{".index(a) == ")]}".index(b)


print(balance("{[(]})"))
# print(balance("(())())"))
