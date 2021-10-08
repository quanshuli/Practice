def move_zeros(array):
    arr = []
    
    for i in array:
        if i != 0:
            arr.append(i)
            
    for i in range(len(array)-len(arr)):
        arr.append(0)
        
    return arr
    
#
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)