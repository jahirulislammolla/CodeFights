def isCaseInsensitivePalindrome(s):
    x=s.lower()
    return x==x[::-1]
