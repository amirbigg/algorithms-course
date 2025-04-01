"""
Search insert
    [1,3,5,6], 5 -> 2
    [1,3,5,6], 2 -> 1
    [1,3,5,6], 7 -> 4
    [1,3,5,6], 0 -> 0
    Complexity: O(log n)
"""
def search_insert(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if target > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return low

print(search_insert([1,3,5,6], 3))
