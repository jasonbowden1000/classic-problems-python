import string

def is_palindrome(str):
    whitelist = set(string.ascii_lowercase)
    str = str.lower()
    str = ''.join([char for char in str if char in whitelist])
    return str == str[::-1]
