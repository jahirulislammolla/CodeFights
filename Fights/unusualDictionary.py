def unusualDictionary(wordList):
    lst = [a.split() for a in wordList]
    lst = [(a[-1], a) for a in lst]
    print(lst)
    return sorted(lst) == lst
