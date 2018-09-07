from fractions import gcd
def videoPart(part, total):
    x=list(map(int,part.split(":")))
    s=x[0]*3600+x[1]*60+x[2]
    x=list(map(int,total.split(":")))
    t=x[0]*3600+x[1]*60+x[2]
    g=gcd(s,t)
    return [s/g,t/g]
    
    

