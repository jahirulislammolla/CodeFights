def firstMultiple2(divisors, start):
     while True:
        for i in divisors:
            if start%i==0:
                return start
        start+=1
