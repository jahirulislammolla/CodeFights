def theJanitor(word):
    y=[0 for i in range(26)]
    x={}
    k=0
    for i in word:
        if ord(i)-97 not in x:
            x[ord(i)-97]=[]
        x[ord(i)-97]+=[k]
        k+=1
    for i in x:
        y[i]=x[i][-1]-x[i][0]+1
    return y
