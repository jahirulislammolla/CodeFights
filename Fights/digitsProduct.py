def digitsProduct(product):

    answerDigits = []
    answer = 0

    if product == 0:
        return 10

    if product == 1:
        return 1

    for divisor in range(9, 1, -1):
        while product % divisor == 0:
            product /= divisor
            answerDigits.append(divisor)

    if product > 1:
        return -1


    for i in range(len(answerDigits) - 1, -1, -1):
        answer=answer*10+answerDigits[i]
    return answer
print(digitsProduct(450))
