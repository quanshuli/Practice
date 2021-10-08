def solution(number):
    if number <= 0:
        return 0
    
    add = 0
    for i in range(number):
        if i % 3 == 0:
            add += i
        elif i % 5 == 0:
            add += i
            
    return add
    
#
def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)