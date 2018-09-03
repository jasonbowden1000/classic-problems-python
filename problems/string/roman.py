from itertools import tee
from functools import reduce

roman_dict = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
    'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'M': 1000
}

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)

def roman_to_arabic(str):
    new_str = list(pairwise(map(lambda x: roman_dict[x], str[::-1])))
    arabic = new_str[0][0]
    for pair in new_str:
        arabic = arabic + pair[1] if pair[0] <= pair[1] else arabic - pair[1]
    return arabic

def arabic_to_roman():
    pass

def is_roman():
    pass
