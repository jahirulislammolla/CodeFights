def squareDigitsSequence(i):
    y=[]
    c=0
    while i not in y:
        c+=1
        y.append(i)
        i=sum(list(map(lambda x:x**2,map(int,list(str(i))))))
    return c
