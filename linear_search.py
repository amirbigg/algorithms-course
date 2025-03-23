"""
Linear (sequential) search
    [1, 2, 5, 9, 3, 20, 54, 62, 12, 8]  20 =>  5
    Complexity: Ω(1), θ(n/2), O(n)
"""

def linear_search(array, element):
    for i, value in enumerate(array):
        if value == element:
            return i
    return -1

print(linear_search([1, 2, 5, 9, 3, 20, 54, 62, 12, 8], 8))
