def lineEncoding(s):

  s += '#'
  cnt = 1
  result = []
  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      cnt += 1
    else:
      if cnt > 1:
        result.append(str(cnt))
      result.append(s[i-1])
      cnt=1

  return ''.join(result)
