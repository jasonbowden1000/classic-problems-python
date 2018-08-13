import math

def reverse_digits(n):
    r = 0;
    sign = 1 if n >= 0 else -1
    n = abs(n)

    while n:
        r = r * 10 + n % 10
        n = math.trunc(n / 10)
    
    return r * sign

