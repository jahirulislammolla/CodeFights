def findProfession(level, pos):
    x=[]
    c=0
    l=level-1
    while l>=0:
        c+=(2**l)
        l-=1
    c+=pos
    l=level
    while l>0:
        x.append(c)
        c//=2
        l-=1
    m="E"
    for i in x[::-1]:
        if i%2==0:
            if m=="E":
                m="E"
            else:
                m="D"
        else:
            if m=="E":
                m="D"
            else:
                m="E"
    if m=="D":
        return "Doctor"
    return "Engineer"
