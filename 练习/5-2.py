def toStr(n, base):
    table = "0123456789abcdef"
    if n < base:
        return table[n]
    else:
        return toStr(n//base)+ table[n%base]

print(toStr(1435, 16))