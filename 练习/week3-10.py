from pythonds.basic.stack import Stack

def dish(a):

    aList = [int(i) for i in a]
    print(aList)
    wash = Stack()
    popOrder = []
    takeOrder = 0
    for i in range(0,10):
        wash.push(i)
        if i == aList[takeOrder]:#如果洗好的最上面的盘子和客户拿的盘子相同
            while not wash.isEmpty() and wash.peek() == aList[takeOrder]:#最上面的盘子和客户拿的盘子相同
                #最上面的盘子和客户拿的盘子相同
                #就一直拿盘子，一直扫描客户
                popOrder.append(wash.pop())
                takeOrder +=1
    while not wash.isEmpty():
        #没拿完的盘子就一起放在队列里
        popOrder.append(wash.pop())
    print(popOrder)
    return "Yes" if popOrder == aList else "No"


print(dish("4321078965"))