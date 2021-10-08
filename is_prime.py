def is_prime(num):
    import math
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num))+3):
        if num % i == 0 and num != i:
            return False
        
    return True