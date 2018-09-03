from functools import reduce

roman_dict = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
    'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'M': 1000
}

def roman_to_arabic(str):
    nums = list(map(lambda x: roman_dict[x], str[::-1]))
    return reduce(lambda x, t: x + t[1] if t[0] <= t[1] else x - t[1], zip(nums, nums[1:]), nums[0])

def arabic_to_roman():
    pass

def is_roman():
    pass
