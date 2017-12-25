def cyclicString(s1):

    for answer in range(1, len(s1)):
        correct = True
        for position in range(len(s1)):
            if s1[position] != s1[position % answer]:
                correct = False
                break
        if correct:
            return answer
    return len(s1)
