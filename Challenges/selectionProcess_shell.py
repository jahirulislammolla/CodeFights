import requests
import mysql.connector
import os
x={}
y={}
for r, d, c in os.walk('/root/devops/'):
    for f in c:
        p=r+"/"+f
        if f not in x:
                x[f]=[]
        x[f]+=[open(p).read()]
z={}
for i in sorted(x):
    z[i]={}
    for j in x[i]:
        m=j.split("\n")
        for k in m[:-1]:
            t=k.split(" ")
            if int(t[-1]) not in z[i]:
                z[i][int(t[-1])]=[]
            z[i][int(t[-1])]+=[k]
for i in sorted(z):
    print(i.split(".")[0]+":")
    c=0
    for j in sorted(z[i],reverse=True):
        for k in sorted(z[i][j]):
            c+=1
            print(' '.join(k.split(" ")[:-1]))
            if c==4:
                break
        if c==4:
            break
    print()
