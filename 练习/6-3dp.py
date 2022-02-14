

def trSum():
    
    dp = [[0 for col in range(21)] for row in range(6)]

    v = [0,3,4,8,8,10]
    w = [0,2,3,4,5,9]
    for i in range(1,6):
        for j in range(1,21):
            if w[i] > j:#超重，不拿i
                dp[i][j]= dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+ v[i])
    print(dp)
    return dp[-1][-1]

print(trSum())
