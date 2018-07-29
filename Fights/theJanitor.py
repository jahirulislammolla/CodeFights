def theJanitor(word):
    y=[0 for i in range(26)]
    x={}
    k=0
    for i in word:
        if ord(i)-97 not in x:
            x[ord(i)-97]=[]
        x[ord(i)-97]+=[k]
        k+=1
    for i in x:
        y[i]=x[i][-1]-x[i][0]+1
    return y

def theJanitor(word):

    left = [0] * 26
    right = [0] * 26
    was = [0] * 26
    for i in range(26):
        left.append(0)
        right.append(0)
        was.append(False)

    for i in range(len(word)):
        c = ord(word[i]) - ord('a')
        if not was[c]:
            was[c]=True
            left[c]=i
        right[c] = i

    ans = []
    for i in range(26):
        ans.append(right[i] - left[i] + 1 if was[i] else 0)
    return ans
