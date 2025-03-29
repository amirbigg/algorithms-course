"""
Jump search
    [3, 7, 15, 61, 79, 104, 500, 619, 892], 79 => 4
    Complexity: O(n^1/2) ~ O(√n)
"""
import math


def jump_search(array, target):
    arr_size = len(array) #9
    block_size = int(math.sqrt(arr_size)) #3
    prev = 0
    step = block_size #3

    while array[min(step, arr_size) - 1] < target:
        prev = step #3
        step += block_size #6
        if prev >= arr_size:
            return -1

    while array[prev] < target:
        prev += 1 #4
        if prev == min(step, arr_size):
            return -1

    if array[prev] == target:
        return prev

    return -1

print(jump_search([3, 7, 15, 61, 79, 104, 500, 619, 892], 600))
