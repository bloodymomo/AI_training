from math import sqrt


res = True
n = int(input())

for i in range(2, int(sqrt(n))+1):
    if n%2 == 0:
        res = False
        break
if res == True:
    print("%d is a prime number" %(n))
else:
    print("%d is a NOT prime number" %(n))
