def reduceString(s):
    a=0
    b=len(s)-1
    while a<b:
        if s[a]==s[b]:
            a+=1
            b-=1
        else:
            b+=1
            break
    return s[a:b]
