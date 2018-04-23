def stringsConstruction(a, b):
    x=[0]*26
    y=[0]*26
    for i in a:
        x[ord(i)-97]+=1
    for i in b:
        y[ord(i)-97]+=1
    m=99999999
    for i,j in zip(x,y):
        if i!=0:
            if j==0:
                return 0
            else:
                m=min(m,j//i)
    return m
