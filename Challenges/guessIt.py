def guessIt(message, options):
    x=[]
    y=[]
    c=''
    for i in  message:
        if i!="$":
            c+=i
        else:
            if c!="":
                x.append(c)
                y.append(c)
                y.append("$")
            else:
                if len(y)==0:
                    y.append("$")
            c=''
    if c!="":
        x.append(c)
    if len(x)==0:
        return options
    pp=[]
    for i in options:
        l=0
        c=0
        d=0
        try:
            while l<=len(i) and c<len(x):
                m=len(x[c])
                if l+m<=len(i) and i[l:l+m]==x[c]:
                    d+=1
                    if d<len(y) and y[d]==x[c]:
                        d+=1
                    c+=1
                    l+=m
                elif l+m<=len(i) and i[l:l+m]!=x[c] and y[d]!="$":
                    break
                else:
                    l+=1
            if c==len(x):
                pp.append(i)
        except:
            continue
    return pp
