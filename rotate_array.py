"""
rotate array
    [32, 10, 43, 17, 9, 51, 80] 3 => [9, 51, 80, 32, 10, 43, 17]
    Complexity: O(nk) - k = steps to rotate
"""
def rotate_array(array, step):
    n = len(array)

    for i in range(step):
        temp = array[n-1]
        for j in range(n-1, 0, -1): #654321
            array[j] = array[j-1]
        array[0] = temp
    return array


print(rotate_array([32, 10, 43, 17, 9, 51, 80], 3))
