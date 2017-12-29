def countWaysToReachFinish(cells):

    n = len(cells)
    MAX_MASK = 1 << n

    # dp[m][k] - the number of ways to reach the k-th cell using jumps
    # that are marked in the mask m.
    dp = []
    was = []
    for m in range(MAX_MASK):
        dp.append([0] * n)
        was.append([False] * n)
    dp[0][0] = 1
    was[0][0] = True

    def get(m, k):
        if k < 0 or k >= n or not cells[k]:
            return 0
        #dp[m][k]=0
        if was[m][k]:
            return dp[m][k]
        for i in range(1, n):
            if (m >> i & 1) == 1:
                dp[m][k] += get(m ^ (1 << i), k - i)
                dp[m][k] += get(m ^ (1 << i), k + i)
        was[m][k] = True
        return dp[m][k]

    ans = 0
    for m in range(0, MAX_MASK):
        ans += get(m, n - 1)

    return ans
