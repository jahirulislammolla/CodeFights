def reverseOddCount(st):
    x={}
    y=[]
    l=len(st)-1
    for i in st:
        try:
            x[i]+=1
        except:
            x[i]=1
        y+=[""]
    for i in range(len(st)):
        if x[st[i]]%2==0:
            y[i]=st[i]
        else:
            while x[st[l]]%2==0:
                l-=1
            y[l]=st[i]
            l-=1
    return ''.join(y)

