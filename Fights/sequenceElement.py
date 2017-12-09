def sequenceElement(a, n):
  r = [a]
  while True:
    b = a[1:5] + [sum(a)%10]
    a = b
    if r[0] == b: break;
    r.append(b)
  return r[n%len(r)][0]
