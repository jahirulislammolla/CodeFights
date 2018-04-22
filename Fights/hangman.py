def hangman(w, l):
   a=[]
   k=0
   c=0
   for i in w:
      if i not in a:
         a.append(i)
   for i in l:
      if i not in a:
         c+=1
         if c is 6:
            return False
      if i  in a:
         k+=1
         if k is len(a):
            return True    
   return False
   #...................
   
   def hangman(w, l):
    n = []
    c = 0
    while c < 6 and l:
        if l[0] in w:
            n+=l[0]
        else:
            c+=1
        l=l[1:]
    return set(n)==set(w)
