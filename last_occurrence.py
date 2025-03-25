"""
Last occurrence
    [2, 2, 2, 3, 3, 4, 4, 5, 5, 6]  4 => 6
    Complexity: O(log n)
"""

def last_occurrence(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = low + (high - low) // 2

        if (array[mid] == target and mid == len(array) - 1) or (array[mid] == target and array[mid+1] > target):
            return mid
        elif array[mid] <= target:
            low = mid + 1
        else:
            high = mid - 1

print(last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 6], 14))
