def iq_test(numbers):
    #your code here
    numbers = numbers.split(' ')
    count_even = 0
    count_odd = 0
    
    for i in range(len(numbers)):
        if int(numbers[i]) % 2 == 0:
            count_even += 1
            mark_even = i
        else:
            count_odd += 1
            mark_odd = i
    
    if count_even == 1:
        return mark_even + 1
    else:
        return mark_odd + 1
        
        
#
def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]
    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
    
#
def iq_test(numbers):
    eo = [int(n)%2 for n in numbers.split()]
    return eo.index(1 if eo.count(0)>1 else 0)+1