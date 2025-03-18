"""
LIMIT

    [1, 2, 3, 4, 5]

        min 3 => [3, 4, 5]

        max 3 => [1, 2, 3]

        max 3, min 3 => [3]
"""

def limit(arr, min_limit=None, max_limit=None):
    min_check = lambda val: True if min_limit is None else (val >= min_limit)
    max_check = lambda val: True if max_limit is None else (val <= max_limit)

    return [val for val in arr if min_check(val) and max_check(val)]


def limit2(arr, min_limit=None, max_limit=None):
    if len(arr) == 0:
        return arr

    if min_limit is None:
        min_limit = min(arr)
    if max_limit is None:
        max_limit = max(arr)

    return list(filter(lambda x: (min_limit <= x <= max_limit), arr))


print(limit2([8, 3, 2, 9, 4, 23], min_limit=5, max_limit=13))
