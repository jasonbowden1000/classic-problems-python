def binary_search(arr, value):
    lower = 0;
    upper = len(arr) - 1
    index = -1

    while upper >= lower:
        middle = (lower + upper) // 2

        if arr[middle] > value:
            upper = middle - 1
        elif arr[middle] < value:
            lower = middle + 1
        else:
            index = middle
            upper = middle - 1

    if index < 0:
        raise ValueError(str(value) + ' is not in list')

    return index
