def repeatedDNASequences(s):
    x={}
    y={"A":0,"C":1,"G":2,"T":3}
    for i in range(len(s)-9):
        m=[0,0,0,0]
        n=[0,0,0,0]
        c={}
        d={}
        mm=0
        for k,t in zip(s[i:i+5],s[i+5:i+10][::-1]):
            if  s[i:i+10] not in x:
                x[s[i:i+10]]=0
            x[s[i:i+10]]+=1
    y=[]
    for i in x:
        if x[i]>9:
            y+=[i]
    return sorted(y)
