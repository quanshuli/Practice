def sym_diff (**args):
    arr = []
    for i in range(0, len(args)):
        arr += args[i].symmetric_difference(args[i])
        
    return arr
