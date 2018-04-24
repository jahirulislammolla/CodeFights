def firstMultiple(divisors, start):
    while True:
        k=0
        for i in divisors:
            if start%i==0:
                k+=1
        if k==len(divisors):
            return start
        start+=1
        
