import string

def nihilistCipher(plaintext, keyword, row, column):
    pol = list(keyword) + [x for x in string.ascii_lowercase if x not in keyword]
    z = pol[-1]
    pol = {x:(2*i+j+11)
        for i in range(0, len(pol), 5)
        for j,x in enumerate(pol[i:i+5])}
    pol[z] = row * 10 + column

    np, nk = len(plaintext), len(keyword)

    return [pol[plaintext[i%np]] + pol[keyword[i%nk]]
        for i in range(max(np, nk))]
