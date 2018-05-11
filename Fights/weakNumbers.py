
def d(n):
    divisor = 0
    if n==1:
        return 1
    limit = n
    for i in range(1,limit):
        if (n%i)==0:
            limit = n/i
            if limit!=1:
                divisor += 1
            divisor += 1
    return divisor

def weakNumbers(n):
    dlist = []
    weakness = []
    for i in range(1,n+1):
        divisor = d(i)
        weakness.append(len([j for j in dlist if divisor <j]))
        dlist.append(d(i))
    
    weakest = max(weakness)
    return [weakest,weakness.count(weakest)]
