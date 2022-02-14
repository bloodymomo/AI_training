from pythonds.basic.stack import Stack

#10进制转2,8,16进制


def trans(n, x):
    rem = Stack()

    if x == 8:
        l = "01234567"  # 8进制字典
    if x == 16:
        l = "0123456789abcdef"  # 16进制字典

    res = ""
    while n != 0:
        r = n % x
        rem.push(r)
        n = n//x

    while not rem.isEmpty():
        if x == 2:
            res = res + str(rem.pop())
        else:
            res = res + l[rem.pop()]
    return res


print(trans(1000, 16))
# print(balance("(())())"))
