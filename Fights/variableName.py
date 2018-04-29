def variableName(name):
    if "0"<=name[0]<="9":
        return False
    for i in name:
        if "0"<=i<="9" or "a"<=i.lower()<="z" or i=="_":
            continue
        else:
            return 0
    return 1
