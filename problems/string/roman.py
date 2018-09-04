from functools import reduce
import re

roman_dict = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
    'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'M': 1000
}

def roman_to_arabic(str):
    nums = list(map(lambda x: roman_dict[x], str[::-1]))
    return reduce(lambda x, t: x + t[1] if t[0] <= t[1] else x - t[1], zip(nums, nums[1:]), nums[0])

def arabic_to_roman(num):
    roman = ''
    for k, v in sorted(roman_dict.items(), key=lambda x: x[1], reverse=True):
        while num >= v:
            roman += k
            num -= v
    return roman

def is_roman(str):
    return re.search('^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', str)
