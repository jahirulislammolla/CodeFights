def cyclicQueue(commands):

    maxSize = 10
    queue = [0] * maxSize
    answer = []
    head = 0
    tail = 0
    currentSum = 0

    for i in range(len(commands)):
        if commands[i] == '-':
            currentSum -= queue[head]
            head = (head + 1) % maxSize
        else:
            value = 0
            for j in range(1, len(commands[i])):
                value = value * 10 + ord(commands[i][j]) - ord('0')
            currentSum += value
            queue[tail] = value
            tail = (tail + 1) % maxSize
        answer.append(currentSum)

    return answer
