"""
m      =  [1,2,3]
          [4,5,6]
          [7,8,9]

T     =   [1,4,7]
          [2,5,8]
          [3,6,9]

F    =    [7,4,1]
          [8,5,2]
          [9,6,3]

Complexity: O(n^2)
"""
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix) # 3

        for r in range(n): # 0 1 2
            for c in range(r, n): # 012 12 2
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]


        for r in range(n): # 0 1 2
            for c in range(n // 2): # 0
                matrix[r][c], matrix[r][n-1-c] = matrix[r][n-1-c], matrix[r][c]
