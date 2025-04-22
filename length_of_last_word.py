class Solution(object):
    def lengthOfLastWord(self, s):
        end_index = len(s) - 1

        while end_index >= 0 and s[end_index] == ' ':
            end_index -= 1
        start_index = end_index
        while start_index >= 0 and s[start_index] != ' ':
            start_index -= 1
        return end_index - start_index
