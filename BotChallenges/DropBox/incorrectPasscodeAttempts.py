def incorrectPasscodeAttempts(passcode, attempts):
    c=0
    ck=0
    for i in attempts:
        if i==passcode:
            c=0
        else:
            c+=1
        if c>=10:
            return 1
    return 0
