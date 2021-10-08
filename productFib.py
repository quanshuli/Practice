def productFib(prod):
    # your code
    from math import sqrt
    g = (1 + 5 ** 0.5) / 2.
    sqrt5 = sqrt(5.)
    n = 2
    
    def xn(n):
        return round((g**n - (1-g)**n) / sqrt5)
    
    while True:
        if xn(n) * xn(n+1) == prod:
            return [xn(n), xn(n+1), True]
        elif xn(n) * xn(n+1) < prod and xn(n+1) * xn(n+2) > prod :
            return [xn(n+1), xn(n+2), False]
        
        n += 1 
# only works for smaller numbers

#
def productFib(prod):
    x0 = 0
    x1 = 1 
    while True:    
        if prod == x0 * x1 :
            return [x0, x1, True]
        elif prod > x0 * x1:
            x = x0 + x1
            x0 = x1
            x1 = x
            
            if prod < x0 * x1 :
                return [x0, x1, False]

#
def productFib(prod):
  a, b = 0, 1
  while prod > a * b:
    a, b = b, a + b
  return [a, b, prod == a * b]