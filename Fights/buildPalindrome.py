def buildPalindrome(st):
    i = len(st)
    while True:
        canConvert = True
        j = 0
        while j < i - j - 1:
            if i - j - 1 < len(st) and st[j] != st[i - j - 1]:
                canConvert = False
                break
            j += 1
        if canConvert:
            for j in range(len(st), i):
                st += st[i - j - 1]
            return st
        i += 1
