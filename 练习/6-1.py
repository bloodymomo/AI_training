#递归找零问题
import time
def recM(coinValueList, change, knowResult): #硬币体系【1,5,10,25】， 找零金额,中间记过表
    minCoins = change#最差结果是63个1分硬币
    if minCoins in coinValueList:
        knowResult[change] = 1
        return 1
    elif knowResult[change] > 0:
        return knowResult[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recM(coinValueList, change-i, knowResult)#递归调用自身，每次+1个coin
            #减小规模，每次减去一种硬币面值挑选最小数量
            
            if numCoins < minCoins:
                minCoins = numCoins
                knowResult[change] = minCoins
         
    return minCoins
    
t1 = time.perf_counter()
memo = [0]*64
print(recM([1,5,10,25], 63, memo))
t2 = time.perf_counter()
print(t2-t1)
print(memo)