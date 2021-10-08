def narcissistic( value ):
    # Code away
    arr = [int(x) for x in str(value)]
    num = 0
        
    for i in range(len(arr)):
        num += arr[i] ** len(arr)
    
    return value == num
    
#
def narcissistic(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))