def zeros(n):
    trail = 0
    while n / 5 > 1:
        trail += int(n/5)
        n = n / 5
    
    trail += int(n/5)
    
    return trail
    
#
def zeros(n):
  x = n/5
  return x+zeros(x) if x else 0