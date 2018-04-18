def longestWord(text):
    s=[]
    d=''
    for i in text:
        if "a"<=i.lower()<="z":
            d+=i
        else:
            if d!="":
                s.append(d)
                d=""
    if d!="":
        s.append(d)
    l=0
    m=''
    for i in s:
        if len(i)>l:
            m=i
            l=len(i)
    return m
