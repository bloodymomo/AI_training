
def uniquePaths(m: int, n: int) -> int:
    # dp = [[0]*n]*m#mxn
    # for i in range(n):
    #     dp[0][i]= 1
    #     print(dp[0][i])
    # for i in range(m):
    #     dp[i][0]= 1
    #     print(dp[i][0])
    # for i in range(1,n):
    #     for j in range(1,m):
    #         dp[j][i]= dp[j-1][i]+dp[j][i-1]
    #         print("{j,i}}")
    #         print((j,i),dp[j][i])
    # print(dp)
    # return dp[m-1][n-1]
    if m ==1 or n ==1:
        return 1
    else:
        return uniquePaths(m-1,n)+uniquePaths(m,n-1)

print(uniquePaths(m=3,n=3))