import requests,os
import mysql.connector
import pandas as pd
x={}
y={}
for r, d, c in os.walk('/root/devops/'):
        for f in c:
                p=r+"/"+f
                if f not in x:
                        x[f]=[]
                x[f]+=[open(p).read()]
#print(x)
k=0
y={}
for i in x:
        if i.split(".")[1]=="log":
                for j in x[i][0].split("\n"):
                        t=j.split("|")
                        if len(t)>2 and t[1]=='ERROR':
                                if t[2] in y:
                                        y[t[2]]+=1
                                else:
                                        y[t[2]]=1
                k+=1
#print(x,y)
for i in sorted(set(y.values()),reverse=True):
        for j in sorted(y.keys()):
                if y[j]==i:
                        print(j+" "+str(i))
        
