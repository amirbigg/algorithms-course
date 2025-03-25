"""
First occurrence
    [2, 2, 2, 3, 3, 4, 4, 5, 5, 6]  4 => 5
"""

def first_occurrence(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2 # INT_MAX + low(which is half of INT_MAX + 1) / 2
        if low == high:
            break

        if array[mid] < target:
            low = mid + 1
        else:
            high = mid

    if array[low] == target:
        return low

print(first_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 6], 60))
