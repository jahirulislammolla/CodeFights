import requests
import mysql.connector
import os
x={}
y={}
for r, d, c in os.walk('/root'):
        for f in c:
                p=r+"/"+f
                if f not in x:
                        x[f]=[]
                x[f]+=[open(p).read()]
        z={}
for i in x:
        for c in range(len(x[i])):
                m=x[i][c].replace("\n"," ").replace(","," ").split(" ")
                for j in m:
                        l=j.split(".")
                        try:
                                if len(l)==4 and all([-1<int(k)<256 for k in l]):
                                        if j in y:
                                                y[j]+=1
                                        else:
                                                y[j]=0
                        except:
                                continue
for i in sorted(y):
        print(i)
        A
