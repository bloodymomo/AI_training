def dpMakeChange(cointValueList, change, minCoins,coinUsed):#minCions动态表, coinUsed,每一步使用的硬币记录
    #从1分开始到change诸葛计算最少硬币数
    for cents in range(1, change+1):
        #1. 初始化一个最大值（全用一分硬币）
        coinCount = cents
        #2. 减去每个硬币，向后查，最少硬币数，同时记录总的最少数
        newCoin = 1
        for j in [c for c in cointValueList if c <= cents]:
            if minCoins[cents - j] + 1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j
        
        minCoins[cents] = coinCount
        coinUsed[cents]= newCoin  
    return minCoins[change]

def track(change, coinUsed):
    res = []
    while change > 0:
        res.append(coinUsed[change])
        change = change - coinUsed[change]
    return res
memo = [0]*64
coinUsed = [0]*64
print(dpMakeChange([5,1,10,21, 25], 63, memo, coinUsed))
print(coinUsed)
print(track(63, coinUsed))