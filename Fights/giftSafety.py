def giftSafety(gift):
    return sum(len(set(gift[i:i+3]))<3 for i in range(len(gift)-2))
