def sum_pairs(ints, s):
    x = 0
    y = 0
    found = False
    for i in range(len(ints)-1,1,-1):
        for j in range(i):
            #print([ints[i], ints[j]])
            if sum([ints[i], ints[j]]) == s:
                x = ints[i]
                y = ints[j]
                found = True
                #print(y,x,s)

    if found:
        return [y, x]
    else:
        return None