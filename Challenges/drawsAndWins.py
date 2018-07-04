def drawsAndWins(teams, points):
    n=teams-1
    a=points//3
    b=points - (a*3)
    x=[]
    while (a+b)<=n and a>-1:
        if a*3+b==points:
            x.append([b,a])
        a-=1
        b=points-(a*3)
    return x
