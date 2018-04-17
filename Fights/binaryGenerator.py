import itertools
def binaryGenerator(s):
    x=[s]
    d=[]
    for i in range(len(s)):
        if s[i]=='0':
            d+=[i]
    for k in range(1,len(d)+1):
        for i in itertools.combinations(d,k):
            m=list(s)
            #print(m,i)
            for j in list(i):
                m[j]="1"
            x.append(''.join(m))
    return sorted(set(x))
        
    

