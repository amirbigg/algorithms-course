class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        result = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[r])
            result = max(result, r-left+1)
        return result
