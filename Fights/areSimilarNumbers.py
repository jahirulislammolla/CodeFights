def areSimilarNumbers(a, b, divisor):
    if a%divisor==b%divisor==0:
        return 1
    if a%divisor==0 and b%divisor!=0:
        return 0
    if b%divisor==0 and a%divisor!=0:
        return 0
    return 1

