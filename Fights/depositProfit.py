def depositProfit(deposit, rate, threshold):
    x=deposit
    c=0
    while x<threshold:
        x=x+(x*rate/100)
        c+=1
    return c
