"""
Find min rotate
    [0 1 2 4 5 6 7] => [4 5 6 7 0 1 2]
    Find the minimum element?
    Complexity: O(log n)
"""

def find_min_rotate(array):
    low = 0
    high = len(array) - 1

    while low < high:
        mid = (low + high) // 2
        if array[mid] > array[high]:
            low = mid + 1
        else:
            high = mid

    return array[low]


print(find_min_rotate([4, 5, 6, 7, 8, 1, 2]))
