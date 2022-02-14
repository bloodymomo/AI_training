def listSum(n):
    if len(n)== 1:
        res = n[0]
    else:
        res = n[0] + listSum(n[1:])
    return res

print(listSum([1,2,3,4,5]))