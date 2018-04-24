def digitalSumSort(a):
    return sorted(a, key=lambda x:[sum(map(int,str(x))),x])
