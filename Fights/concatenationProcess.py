def concatenationProcess(init):
    while len(init) > 1:
        init.sort(key=len)

        j = 1
        while j+1 < len(init) and len(init[j+1]) == len(init[1]):
            j += 1

        a = init[0]
        b = init[j]
        
        init = init[1:j] + init[j+1:] + [a + b]

    return init[0]
