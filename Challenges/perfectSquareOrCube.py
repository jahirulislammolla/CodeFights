from itertools import permutations
def perfectSquareOrCube(n):
    d=0
    n=list(str(n))
    x={}
    for i in permutations(n,len(n)):
        i=int("".join(i))
        if i not in x:
            s=round(i**(1/3),6)
            k=round(i**.5,6)
            if k==int(k) or s==int(s):
                d+=1
            x[i]=0
    return d
        
