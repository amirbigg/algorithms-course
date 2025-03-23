"""
Binary search
    [3, 7, 15, 61, 79, 104, 500, 619, 992], 104 => 5
    Complexity O(log n)
"""

def binary_search(array, element):
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (low + high) // 2
        val = array[mid]
        if val == element:
            return mid

        if val < element:
            low = mid + 1
        else:
            high = mid - 1
    return None

print(binary_search([3, 7, 15, 61, 79, 104, 500, 619, 992], 61))
