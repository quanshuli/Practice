def create_phone_number(n):
    #your code here
    return f"({str(n[0])}{str(n[1])}{str(n[2])}) {n[3]}{n[4]}{n[5]}-{n[6]}{n[7]}{n[8]}{n[9]}"
    
#
def create_phone_number(n):
    m = ''.join(map(str, n))
    return f"({m[:3]}) {m[3:6]}-{m[6:]}"