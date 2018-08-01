import datetime
def resourceCatchUp(logOut, logIn):
    m=str(datetime.timedelta(seconds=logOut[0])).split(", ")[1].split(":")
    n=str(datetime.timedelta(seconds=logIn[0])).split(", ")[1].split(":")
    print(m,n)
    k=int(m[0])
    d=int(n[0])
    o=1
    if int(''.join(m))>int(m[0]+'0000'):
        k+=1
    if k<=d:
        o=0
    k=k%24
    c=0
    while True:
        c+=1
        if k==d:
            break
        k=(k+1)%24
    p=int(str(datetime.timedelta(seconds=logIn[0])).split(", ")[0].split(" ")[0])-int(str(datetime.timedelta(seconds=logOut[0])).split(", ")[0].split(" ")[0])-o
    l=c+p*24
    return (logOut[1]-logIn[1])/l
