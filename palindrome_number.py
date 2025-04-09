class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        original, reversed_ = x, 0
        while x != 0:
            reversed_ = reversed_ * 10 + (x % 10)
            x //= 10

        return original == reversed_


print(Solution().isPalindrome(-121))
