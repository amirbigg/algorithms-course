"""
Two sum
    [2, 11, 7, 15], 9 => [0, 2]
    Complexity: O(n) - omega(1)
"""
def two_sum(numbers, target):
    dic = {}
    for i, num in enumerate(numbers):
        if target - num in dic:
            return [dic[target - num], i]
        dic[num] = i
    return None


print(two_sum([2, 11, 7, 15], 9))
