def isSuspiciousRespondent(ans1, ans2, ans3):
    return (ans1 and ans2 and ans3) or (not ans1 and not ans2 and not ans3)
