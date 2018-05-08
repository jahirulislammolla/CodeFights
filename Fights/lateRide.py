def lateRide(n):
    x=n%60
    a=n//60
    s=0
    while x>0:
        s+=x%10
        x//=10
    while a>0:
        s+=a%10
        a//=10
    return s
