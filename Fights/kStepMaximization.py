from itertools import permutations
def kStepMaximization(n, k):
    x=[n]
    p=0
    while p<k:
        for i in permutations([1,2,3]):
            y=[]
            p+=1
            for t in x:
                c=t
                for j in i:
                    if j==1:
                        e=one(c)
                    elif j==2:
                        e=two(c)
                    else:
                        e=three(c)
                    y.append(e)
            x=y
            if p==k:
                return max(x)
def one(n):
    return n+1
def two(n):
    a=list(str(n))[::-1]
    c=''
    for i in a:
        if i not in "347":
            if i =="6":
                c+="9"
            elif i=="9":
                c+="6"
            else:
                c+=i
    if len(c)==len(a):
        n=int(c)
    return n
def three(n):
    return n*2
print (kStepMaximization(4,9))
