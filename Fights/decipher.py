def decipher(cipher):
    s=''
    x=[]
    for i in cipher:
        s+=i
        if int(s)>=97:
            x.append(int(s))
            s=''
    m=''
    for i in x:
        m+=chr(i)
    return m
