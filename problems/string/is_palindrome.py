def is_palindrome(str):
    i = 0
    j = len(str) - 1
    result = True
    while i < j:
        while ((not str[i].isalpha()) and i < j):
            i += 1
        while ((not str[j].isalpha()) and i < j):
            j -= 1
        if str[i].lower() != str[j].lower():
            result = False
        i += 1
        j -= 1
    return result
