"""
Time complexity: O(n log n * k) - where n is the number of elements in nums,
                                    and k is the average number of digits in those elements

Space complexity: O(n*k)
"""

from functools import cmp_to_key


class Solution(object):
    def largestNumber(self, nums):
        nums_as_str = [str(num) for num in nums] # O(n)
        nums_as_str.sort(key=cmp_to_key(self._compare_numbers)) # O(n log n * k)

        if nums_as_str[0] == "0":
            return "0"

        return "".join(nums_as_str) # O(n*k)

    def _compare_numbers(self, a, b):
        if a + b < b + a: # O(k)
            return 1
        else:
            return -1
