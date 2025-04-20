class Solution(object):
    def myPow(self, x, n):
        def wrapper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            res = wrapper(x, n//2)
            res = res * res
            return x * res if n % 2 else res

        res = wrapper(x, abs(n))
        return res if n >= 0 else 1/res