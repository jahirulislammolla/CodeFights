def sumBelowBound(bound):
    s=0
    k=1
    while s<=bound:
        s+=k
        if s>bound:
            return k-1
        k+=1
