def natural_merge(a):
    runs = []
    temp = [a[0]]
    
    for i in range(1, len(a)):
        if a[i] >= a[i - 1]:
            temp.append(a[i])
        else:
            runs.append(temp)
            temp = [a[i]]
    runs.append(temp)
    
    while len(runs) > 1:
        merged = merge(runs[0], runs[1])
        runs = [merged] + runs[2:]
    
    return runs[0]
