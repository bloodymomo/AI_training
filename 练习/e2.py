

def bool(a, b):
    # aList = sorted(list(a))
    # bList = sorted(list(b))
    # res = True
    # if aList == bList:
    #     return res
    # else:
    #     res = False
    #     return res
    c1 = [0]*26
    c2 = [0]*26

    res = True

    for i in range(len(a)):
        pos = ord(a[i]) - ord('a')
        c1[pos] = c1[pos]+1

    for i in range(len(b)):
        pos = ord(b[i]) - ord('a')
        c2[pos] = c2[pos]+1

    if c1 == c2:
        return res
    else:
        res = False
        return res


print(bool("aabb", "bbab"))
