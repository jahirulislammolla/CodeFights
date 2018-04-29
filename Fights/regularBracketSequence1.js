def regularBracketSequence1(sequence):
    x=[]
    try:
        for i in sequence:
            if i=="(":
                x.append("(")
            else:
               if x.pop()=="(":
                    continue
               else:
                   return 0
        return len(x)==0
    except:
        return 0
            
