def sum_two_smallest_numbers(numbers):
    #your code here
    minv = min(numbers)
    
    numbers.remove(minv)
    
    minv += min(numbers)
    
    return minv
    
#
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])