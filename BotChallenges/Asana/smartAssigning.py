def smartAssigning(names, statuses, projects, tasks):
    k=0
    p=99999999999
    t=99999999999
    for i in range(len(names)):
        if not statuses[i] and t>=tasks[i]:
            if t==tasks[i] and p<=projects[i]:
                continue
            else:
                p=projects[i]
                t=tasks[i]
                k=i
    return names[k]
