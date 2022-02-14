from pythonds.basic.stack import Stack
def unc(lst1):
    s1, s2 = Stack(), Stack()
    for item in lst1:
        s1.push(item)
    lst2 = []
    while not s1.isEmpty():
        ### 在此进行代码填空 ###
        for i in range(s1.pop()):
            print(i)


            s2.push(i)
            #0-8
            #0-6
            #0-4
            #0-2
            #0

        lst2.append(s2.size())
        #9
        #9+7
        #9+7+5
        #9+7+5+3
        #9+7+5+3+1


    return lst2

# 测试
print(unc([1, 3, 5, 7, 9]))
