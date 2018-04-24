def subtractionByRegrouping(m, s):
    c=[]
    e=0
    while m:
        a=m%10
        b=s%10
        if a-e>=b:
            c.append(a-e)
            e=0
        else:
            c.append(a+10-e)
            e=1
        m//=10
        s//=10
    return c
