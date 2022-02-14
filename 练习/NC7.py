#https://www.nowcoder.com/practice/64b4262d4e6d4f6181cd45446a5821ec?tpId=117&&tqId=34928&rp=1&ru=/ta/job-code-high&qru=/ta/job-code-high/question-ranking

#class Solution:
    # def maxProfit(self , prices: List[int]) -> int:
    #     if prices == [] and len(prices) == 0:
    #         return 0
    #     minPrice = prices[0]

    #     maxProfit = 0
    #     for i in range(len(prices)):
    #         if minPrice > prices[i]:
    #             minPrice = prices[i]
    #         if i ==0:
    #             profit = max(0,0 - prices[0])
    #             maxProfit = profit
    #         else:
    #             maxProfit = max(maxProfit, prices[i]-minPrice)
    #     return maxProfit

def maxProfit(prices) -> int:
    if prices == [] and len(prices) == 0:
        return 0
    dp = [[0]*len(prices)]*2
    print(dp)
    dp[0][0] = 0
    dp[0][1] = prices[0]#手上有股票，最小付收益
    for i in range(1, len(prices)):
        dp[i][0] = max(dp[i-1][0], prices[i]-dp[i-1][1])
        dp[i][1] = min(dp[i-1][1], prices[i])
    return dp[len(prices)-1][0]

print(maxProfit([8,9,2,5,4,7,1]))

