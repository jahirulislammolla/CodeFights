def countSumOfTwoRepresentations2(n, l, r):
    c=0
    for i in range(l,r+1):
        b=n-i
        if b <= r and b >= i:
                c+=1
    return c

