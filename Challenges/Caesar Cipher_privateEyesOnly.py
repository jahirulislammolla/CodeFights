
def privateEyesOnly(m):
    p=['TH', 'HE', 'AN', 'RE', 'ER', 'IN', 'ON', 'AT', 'ND', 'ST', 'ES', 'EN', 'OF', 'TE', 'ED', 'OR', 'TI', 'HI', 'AS']
    d=0
    t=0
    for i in range(26):
        x=casear(m,i)
        c=0
        for j in range(1,len(m)):
          if (x[j-1]+x[j]).upper() in p:
            c+=1
          if x[j-1].upper() in "ETAOIN SHRDLU":
            c+=1
        if c>d:
          d=c
          t=i
    return casear(m,t)
def casear(t, k):
  def cipher(i, l=range(97,123), u=range(65,91)):
     if i in l or i in u:
       s = 65 if i in u else 97
       i = (i - s + k) % 26 + s
     return chr(i)
  return ''.join([cipher(ord(s)) for s in t])
