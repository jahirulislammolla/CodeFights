def commonCharacterCount(s1, s2):
    x={}
    y={}
    for i in s1:
        if i not in x:
            x[i]=0
        x[i]+=1
    for i in s2:
        if i not in y:
            y[i]=0
        y[i]+=1
    c=0
    for i in x:
        if i in y:
            c+=min(x[i],y[i])
    return c
