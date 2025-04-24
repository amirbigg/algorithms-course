"""
Selection sort
    - The Selection Sort algorithm finds the lowest value in an array and
    moves it to the front of the array.
    Time Complexity: O(n**2)
    Space Complexity: O(1)
"""

def selection_sort(arr, simulation=False):
    iteration = 0
    if simulation:
        print("Iteration", iteration, ":", *arr)

    for i in range(len(arr)):
        minimum = i

        for j in range(i+1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]

        if simulation:
            iteration += 1
            print("Iteration", iteration, ":", *arr)

    return arr


print(selection_sort([7, 12, 9, 11, 3], simulation=True))
