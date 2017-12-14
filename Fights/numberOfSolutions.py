def numberOfSolutions(n):          
    result = 0
    for a in range(n+1, 2 **n):
        print(a,n) 
        if (a * n) % (a - n) == 1:
            result += 1                        
    return result * 2 + 1 
print(numberOfSolutions(3))
