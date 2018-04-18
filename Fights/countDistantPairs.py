def countDistantPairs(st, d):
    res=0
    for i in range(len(st)-d-1):
        if st[i]==st[i+d+1]:
            res+=1
    return res//2
