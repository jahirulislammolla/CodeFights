def countSumOfTwoRepresentations3(n, l, r):
    return max(n//2-max(l,n-r)+1,0)
