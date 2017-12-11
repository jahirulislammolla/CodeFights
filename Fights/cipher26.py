def cipher26(message):
    s=[message[0]]
    index=ord(message[0])-97
    cip_index=0
    for i in range(1,len(message)):
        a=ord(message[i])-97
        if a>index:
            cip_index=a-index
        else:
            cip_index=(26-index+a)%26
        index=(index+cip_index)%26
        s.append(chr(97+cip_index))
    return "".join(s)
        

