def marathonTaskScore(marathonLength, maxScore, submissions, successfulSubmissionTime):
    lost1=0
    if submissions>1:
        lost1=10*(submissions-1)
    d=maxScore -lost1 - successfulSubmissionTime*(maxScore/2)*(1/marathonLength)
    print(d)
    if successfulSubmissionTime==-1:
        return 0
    if d<maxScore/2:
        return maxScore/2
    return d
