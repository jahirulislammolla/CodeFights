def caseUnification(S):
    cu = len(re.findall('[a-z]', S))
    cl = len(re.findall('[A-Z]', S))
    if (cu == 0 or cl != 0 and cu < cl):
        return S.upper()
    else:
        return S.lower()
