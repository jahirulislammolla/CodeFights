
import urllib.request
import json
def notTheBestFan(contests, yourFavourite):
    def response(url):
        with urllib.request.urlopen(url) as response:
            return response.read()
    m=yourFavourite
    n=yourFavourite
    s=0
    t=0
    for i in contests:
        url = 'http://codeforces.com/api/contest.standings?contestId='+str(i)+'&from=1&count=25'
        res = response(url)
        x=json.loads(res.decode('utf-8'))['result']['rows']
        c=0
        d=0
        e=0
        f=0
        l=''
        for i in range(25):
            k=x[i]['party']['members'][0]['handle']
            if i==0:
                l=k
            if c==0:
                e=i+1
            if d==0:
                f=i+1
            if k==m:
                c=1
            if k==n:
                d=1
        n=l
        s+=e
        t+=f
    return  s-t
    
