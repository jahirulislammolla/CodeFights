def charactersRearrangement(string1, string2):
    characters1 = list(string1)
    characters2 = list(string2)
    correct = True

    characters1.sort()
    characters2.sort()

    for i in range(max(len(characters1), len(characters2))):
        if (i >= len(characters1) or i >= len(characters2)
           or characters1[i] != characters2[i]):
            correct=False
            

    return correct
