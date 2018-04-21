def visitsOnCircularRoad(n, vi):
    res=0
    pre=1
    for i in range(len(vi)):
        first=abs(pre-v[i])
        res+=min(first,abs(n-first))
        pre=vi[
    return res
        
